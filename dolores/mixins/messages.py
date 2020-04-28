from typing import Any
from dolores.mixins.mixinmeta import PlatformMeta
from dolores.platforms.telegram.mixins.message import TgMessagesMixin
from dolores.platforms.vk.mixins.message import VkMessagesMixin
from models.model import UserModel


class MessagesMixin(TgMessagesMixin, VkMessagesMixin, metaclass=PlatformMeta):

    async def send_message(self, user: UserModel, text: str, keyboard: Any = None):
        return await super().send_message(user, text, keyboard)
