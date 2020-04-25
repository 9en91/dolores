from abc import ABCMeta
from core.api.api import VkAPI


class ViewSet(metaclass=ABCMeta):

    api = VkAPI()
    user = None


