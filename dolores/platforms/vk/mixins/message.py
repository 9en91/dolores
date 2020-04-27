from typing import Any
from dolores import utils
from dolores.platforms.base.mixin import BaseMixin
from dolores.platforms.base.protocols.messages import MessagesProtocol
from models.model import UserModel


class VkMessagesMixin(BaseMixin, MessagesProtocol):
    async def send_message(self, user: UserModel, text: str, keyboard: Any = None):
        params = self._build_params_to_api(user_id=user.id,
                                           message=text,
                                           random_id=utils.get_random_id(),
                                           keyboard=keyboard)
        await self.api.messages.send(**params)