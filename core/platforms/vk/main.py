import re
from typing import final

import requests
from vk_api import VkApi
# from vk_api.vk_api import VkApiMethod
from vk_api.vk_api import VkApiMethod

from core.platforms._base.abstract_bot import AbstractBot # noqa
# from core.platforms.vk.method import VkApiMethod
from core.platforms.vk.types.vk_api_ref import VkBotMessageEvent, VkBotEventType, VkBotEvent
from core.types._view_container import _ViewContainer, _MessageContainer # noqa
from settings import TOKEN, ID_BOT # noqa
from core.api.messages import MessagesMixin
from tools.state import State


@final
class VkBot(AbstractBot,
            MessagesMixin):

    #: Классы для событий по типам
    CLASS_BY_EVENT_TYPE = {
        VkBotEventType.MESSAGE_NEW.value: VkBotMessageEvent,
        VkBotEventType.MESSAGE_REPLY.value: VkBotMessageEvent,
        VkBotEventType.MESSAGE_EDIT.value: VkBotMessageEvent,
    }

    #: Класс для событий
    DEFAULT_EVENT_CLASS = VkBotEvent

    def __init__(self):
        super().__init__()
        self.vk = VkApi(token=TOKEN)
        self.api: VkApiMethod = self.vk.get_api()
        self.group_id = ID_BOT
        self.wait = 25

        self.url = None
        self.key = None
        self.server = None
        self.ts = None

        self.session = requests.Session()

        self.update_longpoll_server()


    def _parse_event(self, raw_event):
        event_class = self.CLASS_BY_EVENT_TYPE.get(raw_event['type'],
                                                   self.DEFAULT_EVENT_CLASS)
        return event_class(raw_event)

    def update_longpoll_server(self, update_ts=True):
        values = {'group_id': self.group_id}
        response = self.vk.method('groups.getLongPollServer', values)
        self.key = response['key']
        self.server = response['server']
        self.url = self.server
        if update_ts:
            self.ts = response['ts']

    def check(self):
        values = {
            'act': 'a_check',
            'key': self.key,
            'ts': self.ts,
            'wait': self.wait,
        }

        response = self.session.get(self.url,
                                    params=values,
                                    timeout=self.wait + 10).json()

        if 'failed' not in response:
            self.ts = response['ts']
            return [self._parse_event(raw_event) for raw_event in response['updates']]

        elif response['failed'] == 1:
            self.ts = response['ts']

        elif response['failed'] == 2:
            self.update_longpoll_server(update_ts=False)

        elif response['failed'] == 3:
            self.update_longpoll_server()

        return []

    def listen(self):
        while True:
            for event in self.check():
                yield event

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

