from typing import Any
from dolores import utils
from dolores.platforms.base.mixin import BuilderMixin
from dolores.platforms.base.protocols.messages import MessagesProtocol
from models.model import UserModel


class TgMessagesMixin(BuilderMixin, MessagesProtocol):
    async def send_message(self, user: UserModel, text: str, keyboard: Any = None):
        params = self._build(chat_id=user.id,
                             text=text,
                             keyboard=keyboard)
        return await self.api.sendMessage(**params)
