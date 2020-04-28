import asyncio
from typing import List, NoReturn
from dolores.platforms.base.bot import AbstractBot
from dolores.platforms.vk.api import VkAPI
from dolores.platforms.vk.schema.schema import ResponseSchema
from dolores.platforms.vk.types.message import VkResponseType
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
                return self.longpoll_schema.load(response["updates"], many=True)
            elif response["failed"] == 1:
                self.ts = response["ts"]
            elif response["failed"] == 2:
                await self._update_longpoll_server(update_ts=False)
            elif response["failed"] == 3:
                await self._update_longpoll_server()
            return []

    async def polling(self) -> NoReturn:
        self._polling = True
        await self._update_longpoll_server()
        while self._polling:
            for update in await self.get_updates():
                if update.type_response != "message_new":
                    continue
                message = update.object_response.message
                user_id = message.from_id
                text = message.text
                asyncio.create_task(self.execute(message, user_id, text))
