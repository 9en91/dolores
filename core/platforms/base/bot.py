import asyncio
from abc import ABCMeta

import aiohttp

from core.platforms.vk.types.message import VkResponseType


class AbstractBot(metaclass=ABCMeta):

    def __init__(self, loop: asyncio.ProactorEventLoop):
        print("starting bot...")

        self.loop = loop
        _handlers = {}
        self.__user_model = None
        self.__post_init()

        self.session = aiohttp.ClientSession()

    def __post_init(self):
        from core.const import Consts
        self._handlers = Consts.views
        self.__user_model = Consts.user_model

    def _init_user(self, event: VkResponseType):
        user, created = self.__user_model.get_or_create(id=event.object_response.message.from_id)
        return user
