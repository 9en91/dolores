from typing import Any, Callable
from dolores import utils
from dolores.exceptions import ApiException
from dolores.platforms.base.mixin import BuilderMixin
from dolores.platforms.base.protocols.messages import MessagesProtocol


class VkMessagesMixin(BuilderMixin, MessagesProtocol):

    async def send_message(self, user: Any, text: str, keyboard: Any = None, callback: Callable = None):
        params = self._build(user_id=user.id,
                             message=text,
                             random_id=utils.get_random_id(),
                             keyboard=keyboard)
        try:
            return await self.api.messages.send(**params)
        except ApiException as e:
            if callback is not None:
                return await callback()
            else:
                raise e
