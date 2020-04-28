import asyncio
import re
from typing import List, Tuple, Any, NoReturn

from dolores.const import Consts
from dolores.platforms.base.bot import AbstractBot
from dolores.platforms.telegram.api import TgAPI
from dolores.platforms.telegram.schema.schema import ResponseSchema
from dolores.platforms.telegram.types.types import TgResultsType


class TgBot(AbstractBot):

    def __init__(self):
        super().__init__()
        self.api = TgAPI(token=self.token, session=self.session)
        self.offset = None
        self.limit = None
        self.timeout = 20

        self.builder = self.api.build()
        self.longpoll_schema = ResponseSchema()

    async def get_updates(self) -> List[TgResultsType]:
        params = {"limit": self.limit, "offset": self.offset, "timeout": self.timeout}
        result = await self.builder.getUpdates(**params)
        return self.longpoll_schema.load(result).result

    async def polling(self) -> NoReturn:
        self._polling = True
        while self._polling:
            for update in await self.get_updates():
                message = update.message
                user_id = message.from_user.from_id
                text = message.text
                asyncio.create_task(self.execute(message, user_id, text))
                self.offset = update.update_id + 1
