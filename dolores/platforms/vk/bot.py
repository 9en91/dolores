import asyncio
import re
from typing import List, Optional
from dolores.platforms.base.bot import AbstractBot
from dolores.platforms.vk.api import VkAPI
from dolores.platforms.vk.schema.schema import ResponseSchema
from dolores.platforms.vk.types.message import VkResponseType
from settings import TOKEN, ID_BOT
from dolores.const import Consts


# @final
class VkBot(AbstractBot):

    def __init__(self):
        super().__init__()
        self.url = None
        self.key = None
        self.ts = None

        self.api = VkAPI(token=TOKEN, session=self.session)
        self.builder = self.api.build()
        self.group_id = ID_BOT
        self.wait = 25

        self.longpoll_schema = ResponseSchema()

    async def update_longpoll_server(self, update_ts=True):
        values = {"group_id": self.group_id}
        response = await self.api.method("groups.getLongPollServer", values)
        response = response["response"]
        self.key = response["key"]
        self.url = response["server"]
        if update_ts:
            self.ts = response["ts"]

    async def get_updates(self) -> List[Optional[VkResponseType]]:

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

    async def _init_event(self, event):
        user = await self._init_user(event.object_response.message.from_id)
        text = event.object_response.message.text
        state = Consts.STATE(user.state)
        return user, state, text

    async def polling(self):
        await self.update_longpoll_server()
        while True:
            for update in await self.get_updates():

                if update.type_response != "message_new":
                    continue

                user, state, text = await self._init_event(update)

                if state in self._handlers:
                    view_handler = self._handlers[state]
                    for message_handler in view_handler.mcl:
                        if re.search(message_handler.regex, text):
                            view_handler.cls.user = user
                            await view_handler.cls.__getattribute__(
                                message_handler.method
                            )(
                                update.object_response.message
                            )
                            break
