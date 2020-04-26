import re
from typing import final

from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.vk_api import VkApiMethod
from core.database.default import BaseUserModel
from core.decorators import Entity, ViewHandler
from core.types._view_container import _ViewContainer, _MessageContainer
from core.utils._loader import _Loader
from settings import TOKEN, ID_BOT
from core.api.messages import MessagesMixin
from tools.state import State


@final
class VkBot(VkBotLongPoll,
            MessagesMixin):

    vk = VkApi(token=TOKEN)
    api: VkApiMethod = vk.get_api()
    _handlers = {}

    def __post_init(self):
        _Loader.load_models()
        _Loader.load_views()
        self._handlers = ViewHandler._handlers
        self.__user_model = Entity.User.model

    def __init__(self):
        print("starting...")
        super().__init__(self.vk, ID_BOT)
        self.__post_init()

    def _init_user(self, event) -> BaseUserModel:
        user, created = self.__user_model.get_or_create(id=event.message.from_id)
        return user

    def polling(self):
        for event in self.listen():
            if event.type != VkBotEventType.MESSAGE_NEW:
                continue
            user = self._init_user(event)
            text = event.message.text
            state = State(user.state)
            if state in self._handlers:
                view_handler: _ViewContainer = self._handlers[state]
                message_handler: _MessageContainer
                for message_handler in view_handler.mcl:
                    if re.search(message_handler.regex, text):
                        view_handler.cls.user = user
                        view_handler.cls.__getattribute__(message_handler.method)(event)
                        break
