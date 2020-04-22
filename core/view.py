from abc import ABCMeta, abstractmethod
from typing import TypeVar, Type, Generic

from core.api.api import VkAPI


class View(metaclass=ABCMeta):

    api = VkAPI()
    user = None

    def __init__(self, event, user):
        self.event = event
        self.user = user

