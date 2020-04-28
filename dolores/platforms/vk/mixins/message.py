from typing import Any
from dolores import utils
from dolores.platforms.base.mixin import BuilderMixin
from dolores.platforms.base.protocols.messages import MessagesProtocol
from models.model import UserModel


class VkMessagesMixin(BuilderMixin, MessagesProtocol):
    async def send_message(self, user: UserModel, text: str, keyboard: Any = None):
        params = self._build(user_id=user.id,
                             message=text,
                             random_id=utils.get_random_id(),
                             keyboard=keyboard)
        return await self.api.messages.send(**params)
