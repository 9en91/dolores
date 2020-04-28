import asyncio
import re
from abc import ABCMeta, abstractmethod
from typing import Tuple, Any, NoReturn, List, Union

import aiohttp

from dolores.const import Consts
from dolores.platforms.telegram.types.types import TgResultsType
from dolores.platforms.vk.types.message import VkResponseType
from settings import ID_BOT, TOKEN


class AbstractBot(metaclass=ABCMeta):

    def __init__(self):
        print("starting bot...")

        self._polling = False
        self._handlers = None
        self._user_model = None
        self.group_id = ID_BOT
        self.token = TOKEN
        self.session = aiohttp.ClientSession()
        self._post_init()

    def _post_init(self):
        from dolores.const import Consts
        self._handlers = Consts.views
        self.__user_model = Consts.user_model

    async def _init_user(self, user_id: int):
        user, created = await self.__user_model.get_or_create(id=user_id)
        return user

    async def _init_event(self, user_id: int) -> Tuple[Any, Any]:
        user = await self._init_user(user_id)
        state = Consts.STATE(user.state)
        return user, state

    async def execute(self, message, user_id, text):
        user, state = await self._init_event(user_id)
        if state in self._handlers:
            view_handler = self._handlers[state]
            for message_handler in view_handler.mcl:
                if re.search(message_handler.regex, text):
                    view_handler.cls.user = user
                    task = view_handler.cls.__getattribute__(message_handler.method)
                    asyncio.create_task(task(message))
                    break

    @abstractmethod
    def get_updates(self) -> List[Union[TgResultsType, VkResponseType]]:
        pass

    @abstractmethod
    def polling(self) -> NoReturn:
        pass

    def __del__(self):
        asyncio.create_task(self.close())

    async def close(self):
        if not self.session.closed:
            await self.session.close()
