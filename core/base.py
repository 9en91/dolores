import re
from typing import List, Optional, Dict
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotMessageEvent, VkBotEventType
from vk_api.vk_api import VkApiMethod

from core.database.default import DefaultUserModel
from core.types._param_handler import ViewContainer, MessageContainer
from core.utils import Utils
from settings import TOKEN, ID_BOT
from core.api.messages import MessagesMixin
from utils.state import State


class Application(VkBotLongPoll, MessagesMixin):
    vk = VkApi(token=TOKEN)
    api: VkApiMethod = vk.get_api()
    _handlers = {}

    def __init__(self):
        print("starting...")
        super().__init__(self.vk, ID_BOT)
        Utils.load_views()
        print()

    def _init_user(self, event) -> DefaultUserModel:
        user, created = DefaultUserModel.get_or_create(id=event.message.from_id)
        return user

    def polling(self):
        for event in self.listen():
            if event.type != VkBotEventType.MESSAGE_NEW:
                continue
            user = self._init_user(event)
            text = event.message.text
            state = State(user.state)
            if state in self._handlers:
                view_handler: ViewContainer = self._handlers[state]
                message_handler: MessageContainer
                for message_handler in view_handler.mcl:
                    if re.search(message_handler.regex, text):
                        view_handler.cls.user = user
                        view_handler.cls.__getattribute__(message_handler.method)(event)

bot = Application
