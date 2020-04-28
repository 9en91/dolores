from typing import Any, Generic, TypeVar
from dolores.platforms import PLATFORMS
from dolores.platforms.base.protocols.messages import MessagesProtocol
from dolores.platforms.telegram.mixins.message import TgMessagesMixin
from dolores.platforms.vk.mixins.message import VkMessagesMixin
from dolores.views import View
from models.model import UserModel
import settings


class PlatformMixin(type):

    def __new__(mcs, name, bases, namespace):
        if issubclass(mcs, View):
            return super(PlatformMixin, mcs).__new__(mcs, name, bases, namespace)
        if settings.PLATFORM == PLATFORMS.VK:
            cls_platform = VkMessagesMixin
        elif settings.PLATFORM == PLATFORMS.TELEGRAM:
            cls_platform = TgMessagesMixin
        else:
            raise Exception
        return super(PlatformMixin, mcs).__new__(mcs, name, (cls_platform,), namespace)

    def __init__(cls, name, bases, namespace):
        if not issubclass(cls, View):
            if settings.PLATFORM == PLATFORMS.VK:
                bases = (VkMessagesMixin,)
            elif settings.PLATFORM == PLATFORMS.TELEGRAM:
                bases = (TgMessagesMixin,)
            else:
                raise Exception
        super().__init__(name, bases, namespace)


class MessagesMixin(TgMessagesMixin, VkMessagesMixin, metaclass=PlatformMixin):

    async def send_message(self, user: UserModel, text: str, keyboard: Any = None):
        print(super().send_message)
        return await super().send_message(user, text, keyboard)
