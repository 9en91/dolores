import asyncio
import re
from typing import final, Dict, List, Optional
import aiohttp
from core.platforms.base.bot import AbstractBot
from core.platforms.vk.api import VkAPI
from core.platforms.vk.schema.schema import ResponseSchema
from core.platforms.vk.types.message import Response
from core.types._view_container import _ViewContainer, _MessageContainer  # noqa
from settings import TOKEN, ID_BOT
from core.api.messages import MessagesMixin
from core.const import _Consts


@final
class VkBot(AbstractBot):

    def __init__(self, loop):
        super().__init__(loop)
        self.url = None
        self.key = None
        self.ts = None

        self.session = aiohttp.ClientSession()
        self.api = VkAPI(token=TOKEN, session=self.session)
        self.builder = self.api.build()
        self.group_id = ID_BOT
        self.wait = 25

    async def update_longpoll_server(self, update_ts=True):
        values = {"group_id": self.group_id}
        response = await self.api.method("groups.getLongPollServer", values)
        response = response["response"]
        self.key = response["key"]
        self.url = response["server"]
        if update_ts:
            self.ts = response["ts"]

    async def check(self) -> List[Optional[Dict]]:
        response = await self.session.get(self.url,
                                          params={
                                              "act": "a_check",
                                              "key": self.key,
                                              "ts": self.ts,
                                              "wait": self.wait,
                                          },
                                          timeout=self.wait + 10)
        response = await response.json()

        if "failed" not in response:
            self.ts = response["ts"]
            return response["updates"]

        elif response["failed"] == 1:
            self.ts = response["ts"]

        elif response["failed"] == 2:
            await self.update_longpoll_server(update_ts=False)

        elif response["failed"] == 3:
            await self.update_longpoll_server()

        return []

    async def polling(self):
        await self.update_longpoll_server()
        schema = ResponseSchema()
        while True:
            for raw_event in await self.check():
                event: Response = schema.load(raw_event)
                if event.type_response != "message_new":
                    continue

                user = self._init_user(event)
                text = event.object_response.message.text

                state = _Consts._STATE(user.state)
                if state in self._handlers:
                    view_handler: _ViewContainer = self._handlers[state]
                    message_handler: _MessageContainer
                    for message_handler in view_handler.mcl:
                        if re.search(message_handler.regex, text):
                            view_handler.cls.user = user
                            await view_handler.cls.__getattribute__(
                                message_handler.method
                            )(event.object_response.message)
                            break

    def __del__(self):
        asyncio.create_task(self._close())

    async def _close(self):
        if not self.session.closed:
            await self.session.close()

    async def _start(self):
        await self.update_longpoll_server()