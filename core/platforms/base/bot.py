import asyncio
from abc import ABCMeta

from core.platforms.vk.types.message import Response


class AbstractBot(metaclass=ABCMeta):

    def __init__(self, loop: asyncio.ProactorEventLoop):
        print("starting bot...")

        self.loop = loop
        _handlers = {}
        self.__user_model = None
        self.__post_init()

    def __post_init(self):
        from core.const import _Consts
        self._handlers = _Consts._views
        self.__user_model = _Consts._user_model

    def _init_user(self, event: Response):
        user, created = self.__user_model.get_or_create(id=event.object_response.message.from_id)
        return user