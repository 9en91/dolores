from typing import Any
from dolores import utils
from dolores.platforms import PLATFORMS
from dolores.platforms.base.mixin import BaseMixin
from dolores.platforms.base.protocols.messages import MessagesProtocol
from dolores.platforms.telegram.mixins.message import TgMessagesMixin
from dolores.platforms.vk.mixins.message import VkMessagesMixin
from models.model import UserModel
import settings


class MessagesMixin(VkMessagesMixin, TgMessagesMixin):
    def __init__(self):
        if settings.PLATFORM == PLATFORMS.VK:
            self.base = VkMessagesMixin
        elif settings.PLATFORM == PLATFORMS.TELEGRAM:
            self.base = TgMessagesMixin

    async def send_message(self, user: UserModel, text: str, keyboard: Any = None):
        for i in self.__class__.__mro__:
            if i == self.base:
                await i.send_message(self, user, text)
