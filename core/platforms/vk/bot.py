import asyncio
import re
from typing import final, List, Optional
from core.platforms.base.bot import AbstractBot
from core.platforms.vk.api import VkAPI
from core.platforms.vk.schema.schema import ResponseSchema
from core.platforms.vk.types.message import VkResponseType
from core.utils.view_container import ViewContainer, MessageContainer  # noqa
from settings import TOKEN, ID_BOT
from core.const import Consts


@final
class VkBot(AbstractBot):

    def __init__(self, loop):
        super().__init__(loop)
        self.url = None
        self.key = None
        self.ts = None

        self.api = VkAPI(token=TOKEN, session=self.session)
        self.builder = self.api.build()
        self.group_id = ID_BOT
        self.wait = 25

        self.longpoll_schema =  ResponseSchema()

    async def update_longpoll_server(self, update_ts=True):
        values = {"group_id": self.group_id}
        response = await self.api.method("groups.getLongPollServer", values)
        response = response["response"]
        self.key = response["key"]
        self.url = response["server"]
        if update_ts:
            self.ts = response["ts"]

    async def check(self) -> List[Optional[VkResponseType]]:

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
            return self.longpoll_schema.load(response["updates"], many=True)

        elif response["failed"] == 1:
            self.ts = response["ts"]

        elif response["failed"] == 2:
            await self.update_longpoll_server(update_ts=False)

        elif response["failed"] == 3:
            await self.update_longpoll_server()

        return []

    def _init_event(self, event):
        user = self._init_user(event)
        text = event.object_response.message.text
        state = Consts.STATE(user.state)
        return user, state, text

    async def polling(self):
        await self.update_longpoll_server()
        while True:
            for event in await self.check():

                if event.type_response != "message_new":
                    continue

                user, state, text = self._init_event(event)

                if state in self._handlers:
                    view_handler = self._handlers[state]
                    for message_handler in view_handler.mcl:
                        if re.search(message_handler.regex, text):
                            view_handler.cls.user = user
                            await view_handler.cls.__getattribute__(message_handler.method)(event.object_response.message)
                            break

    def __del__(self):
        asyncio.create_task(self._close())

    async def _close(self):
        if not self.session.closed:
            await self.session.close()

    async def _start(self):
        await self.update_longpoll_server()
