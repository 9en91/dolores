from enum import IntEnum
from functools import wraps
from typing import List, Optional, Dict

from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotMessageEvent, VkBotEventType
from vk_api.vk_api import VkApiMethod

from core.types._param_handler import _Handler
from core.utils import Utils
from settings import TOKEN, ID_BOT
# from core.mixins.messages import MessagesMixin
# from database.models import Users
# from util.enums.state import States
# from core.events import EventMessage
from core.api.messages import MessagesMixin
# from core.event import Event
from core.view import View
from models.model import UserModel

from utils.state import State


class Application(VkBotLongPoll, MessagesMixin):
    vk = VkApi(token=TOKEN)
    api: VkApiMethod = vk.get_api()
    _handlers: Dict[State, List[_Handler]] = {}

    def __init__(self):
        print("starting...")
        super().__init__(self.vk, ID_BOT)
        Utils.load_views()

    def __filter(self, event):
        if handler in self.__handlers:
            pass
            # if handler.check():
            #     handler.handle(event)
            #     break

    def polling(self):
        for event in self.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:

                self.__filter(event)


bot = Application
