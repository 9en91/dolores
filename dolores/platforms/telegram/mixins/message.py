from typing import Any
from dolores import utils
from dolores.platforms.base.mixin import BaseMixin
from dolores.platforms.base.protocols.messages import MessagesProtocol
from models.model import UserModel


class TgMessagesMixin(BaseMixin, MessagesProtocol):
    async def send_message(self, user: UserModel, text: str, keyboard: Any = None):
        params = self._build_params_to_api(chat_id=user.id,
                                           text=text,
                                           keyboard=keyboard)
        await self.api.sendMessage(**params)
