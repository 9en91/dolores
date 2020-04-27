import re
import typing
from dolores.const import Consts
from dolores.platforms.base.bot import AbstractBot
from dolores.platforms.telegram.api import TgAPI
from dolores.platforms.telegram.schema.schema import ResponseSchema
from dolores.platforms.telegram.types.types import TgResultsType
from settings import TOKEN, ID_BOT


class TgBot(AbstractBot):

    def __init__(self):
        super().__init__()
        self.api = TgAPI(token=TOKEN, session=self.session)
        self.builder = self.api.build()
        self.group_id = ID_BOT
        self.limit = None
        self.timeout = 20
        self.offset = None
        self.longpoll_schema = ResponseSchema()

    async def _init_event(self, update):
        user = await self._init_user(update.message.from_user.from_id)
        text = update.message.text
        state = Consts.STATE(user.state)
        return user, state, text

    async def get_updates(self) -> typing.List[TgResultsType]:
        params = {"limit": self.limit, "offset": self.offset, "timeout": self.timeout}
        result = await self.api.method("getUpdates", params)
        return self.longpoll_schema.load(result).result

    async def polling(self):
        self._polling = True
        while self._polling:
            for update in await self.get_updates():
                user, state, text = await self._init_event(update)
                if state in self._handlers:
                    view_handler = self._handlers[state]
                    for message_handler in view_handler.mcl:
                        if re.search(message_handler.regex, text):
                            view_handler.cls.user = user
                            await view_handler.cls.__getattribute__(message_handler.method)(update.message)
                            break
                self.offset = update.update_id + 1
