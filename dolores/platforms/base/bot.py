from abc import ABCMeta, abstractmethod
from typing import Tuple, Any, NoReturn, List, Union

import aiohttp
from dolores.const import consts
from dolores.platforms.telegram.types.types import TgResultsType
from dolores.platforms.vk.types.message import VkResponseType
from settings import ID_BOT, TOKEN


class AbstractBot(metaclass=ABCMeta):

    def __init__(self):
        print("starting bot...")
        self.api = None
        self.builder = None
        self._polling = False
        self._handlers = None
        self._user_model = None
        self.group_id = ID_BOT
        self.token = TOKEN
        self.session = aiohttp.ClientSession()
        self._post_init()

    def _post_init(self):

        self._handlers = consts.get_views()
        self.__user_model = consts.get_user_model()

    async def _init_user(self, user_id: int):
        user, created = await self.__user_model.get_or_create(id=user_id)
        return user

    async def _init_event(self, user_id: int) -> Tuple[Any, Any]:
        user = await self._init_user(user_id)
        state = consts.get_state()(user._state)
        return user, state

    def handle_middleware(self, response):
        for middleware in consts.get_middleware():
            response = middleware().process(response)
        return response

    @abstractmethod
    async def execute(self, message, user_id, text, update):
        pass

    @abstractmethod
    async def get_updates(self) -> List[Union[TgResultsType, VkResponseType]]:
        pass

    @abstractmethod
    async def polling(self) -> NoReturn:
        pass

    async def close(self):
        await self.session.close()
