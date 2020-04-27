import asyncio
from abc import ABCMeta

import aiohttp
import peewee_async

from dolores.models.connector import DatabaseConnector
from dolores.platforms.vk.types.message import VkResponseType


class AbstractBot(metaclass=ABCMeta):

    def __init__(self):
        print("starting bot...")

        self._polling = False
        self._handlers = None
        self._user_model = None
        self._post_init()

        self.session = aiohttp.ClientSession()

    def _post_init(self):
        from dolores.const import Consts
        self._handlers = Consts.views
        self.__user_model = Consts.user_model

    async def _init_user(self, user_id: int):
        user, created = await self.__user_model.get_or_create(id=user_id)
        return user

    def __del__(self):
        loop = asyncio.new_event_loop()
        loop.run_until_complete(self.close())

    async def close(self):
        await self.session.close()
