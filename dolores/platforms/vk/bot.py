import asyncio
import re
from typing import List, NoReturn

from dolores.const import consts
from dolores.platforms.base.bot import AbstractBot
from dolores.platforms.enums.content import VkContent
from dolores.platforms.enums.events import VkMessageEvents
from dolores.platforms.vk.api import VkAPI
from dolores.platforms.vk.schema.schema import ResponseSchema
from dolores.platforms.vk.types.message import VkResponseType, VkMessageType
from settings import TOKEN


class VkBot(AbstractBot):

    def __init__(self):
        super().__init__()
        self.api = VkAPI(token=TOKEN)
        self.url = None
        self.key = None
        self.ts = None
        self.wait = 25
        self.builder = self.api.build()
        self.longpoll_schema = ResponseSchema()



    async def _update_longpoll_server(self, update_ts: bool = True) -> None:
        values = {"group_id": self.group_id}
        response = await self.builder.groups.getLongPollServer(**values)
        response = self.handle_middleware(response)

        # TODO: add handler middleware

        response = response["response"]
        self.key = response["key"]
        self.url = response["server"]
        if update_ts:
            self.ts = response["ts"]

    async def get_updates(self) -> List[VkResponseType]:
        async with await self.session.get(self.url, params={
            "act": "a_check",
            "key": self.key,
            "ts": self.ts,
            "wait": self.wait,
        }, timeout=self.wait + 10) as response:
            response = await response.json()
            if "failed" not in response:
                self.ts = response["ts"]
                print(response["updates"])
                return self.longpoll_schema.load(response["updates"], many=True)
            elif response["failed"] == 1:
                self.ts = response["ts"]
            elif response["failed"] == 2:
                await self._update_longpoll_server(update_ts=False)
            elif response["failed"] == 3:
                await self._update_longpoll_server()
            return []

    def vk_get_type_message(self, message: VkMessageType):
        types = set()
        if message.text and message.text != "":
            types.add(VkContent.text)
        if message.attachments:
            for i in message.attachments:
                types.add(VkContent(i.attach_type))
        return list(types)

    async def execute(self, message, user_id, text, update):
        types = self.vk_get_type_message(message)
        user, state = await self._init_event(user_id)
        if state in self._handlers:
            view_handler = self._handlers[state]
            for message_handler in view_handler.mcl:
                if re.search(message_handler.regex, text):
                    if types == message_handler.content:
                        view_handler.cls.user = user
                        view_handler.cls.api = self.builder
                        task = view_handler.cls.__getattribute__(message_handler.method)
                        asyncio.create_task(task(message))
                        break

    async def polling(self) -> NoReturn:
        self._polling = True
        await self._update_longpoll_server()
        while self._polling:
            for update in await self.get_updates():

                # message = update.object_response.message
                # user_id = message.from_id
                # text = message.text
                asyncio.create_task(self.execute(message, user_id, text, update))
