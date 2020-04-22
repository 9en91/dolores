from enum import IntEnum
from typing import List, TypeAlias

from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotMessageEvent, VkBotEventType
from vk_api.vk_api import VkApiMethod

from settings import TOKEN, ID_BOT
# from core.mixins.messages import MessagesMixin
# from database.models import Users
# from util.enums.state import States
# from core.events import EventMessage
from core.api.messages import MessagesMixin
# from core.event import Event
from core.view import View
from models.model import UserModel


class Application(VkBotLongPoll, MessagesMixin):
    vk = VkApi(token=TOKEN)
    api: VkApiMethod = vk.get_api()
    __handlers: List[View] = []

    @classmethod
    def view(cls, state):
        def wrapper(view_cls):
            cls.__handlers.append(view_cls)
        return wrapper

    def __init__(self):
        print("starting...")
        super().__init__(self.vk, ID_BOT)

    def __filter(self, event):
        for handler in self.__handlers:
            pass
            # if handler.check():
            #     handler.handle(event)
            #     break

    def polling(self):
        for event in self.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                self.__filter(event)


bot = TypeAlias(Application)
