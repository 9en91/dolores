from abc import ABCMeta, abstractmethod
from typing import TypeVar, Type, Generic

from core.api.api import VkAPI


class View(metaclass=ABCMeta):

    state = None
    text = None
    api = VkAPI()

    _user = None
    _is_new_user = None

    @property
    def user(self):
        return self._user

