from abc import ABCMeta, abstractmethod

from core.api.api import VkAPI
from core.const import _USER_MODEL


class View(metaclass=ABCMeta):
    state = None
    text = None
    api = VkAPI()

    _user: _USER_MODEL = None
    _is_new_user = None

    @property
    def user(self):
        return self._user

    # def handle(self, event):
    #     self._user, _is_new_user = USER_MODEL.get_or_create(id=event.obj.from_id)
    #     self._user.is_new_user = _is_new_user
    #     self.reply(event)
