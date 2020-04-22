from typing import List, Optional, Dict
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotMessageEvent, VkBotEventType
from vk_api.vk_api import VkApiMethod

from core.database.default import DefaultUserModel
from core.types._param_handler import _Handler
from core.utils import Utils
from settings import TOKEN, ID_BOT
from core.api.messages import MessagesMixin
from utils.state import State


class Application(VkBotLongPoll, MessagesMixin):
    vk = VkApi(token=TOKEN)
    api: VkApiMethod = vk.get_api()
    _handlers: Dict[State, List[_Handler]] = {}

    def __init__(self):
        print("starting...")
        super().__init__(self.vk, ID_BOT)
        Utils.load_views()

    def _init_user(self, event) -> DefaultUserModel:
        user, created = DefaultUserModel.get_or_create(id=event.message.from_id)
        return user

    def polling(self):
        for event in self.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                user = self._init_user(event)
                text = event.message.text
                if State(user.state) in self._handlers:
                    for i in self._handlers[user.state]:
                        if text == i.regex:
                            i.fun()


bot = Application
