from __future__ import annotations
from abc import ABCMeta, abstractmethod


class View(metaclass=ABCMeta):
    _state = None
    _event = None
    _text = None
    _content = None
    _api = None

    _next = None

    def add_next(self, view):
        self._next = view

    def get_next(self, view):
        self._next = view

    def get_api(self):
        return self._api

    def set_api(self, api):
        self._api = api

    def get_content(self):
        return self._content

    def set_content(self, content):
        self._content = content

    def get_text(self):
        return self._text

    def set_text(self, text):
        self._text = text

    def get_event(self):
        return self._event

    def set_event(self, event):
        self._event = event

    def get_state(self):
        return self._state

    def set_state(self, state):
        self._state = state

    @abstractmethod
    async def handle(self, message, user, *args, **kwargs) -> None:
        pass
