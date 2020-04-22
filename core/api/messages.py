from typing import Any
from vk_api import utils
from core.api.base import BaseMixin


class MessagesMixin(BaseMixin):
    def send_message(self, user, text: str, keyboard: Any = None):
        params = self._build_params_to_api(user_id=user.id,
                                           message=text,
                                           random_id=utils.get_random_id(),
                                           keyboard=keyboard)
        self.api.messages.send(**params)
