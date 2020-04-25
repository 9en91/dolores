import re
from typing import Pattern, Callable

from core.platforms.vk.vk_bot import VkBot
from core.types._view_container import _ViewContainer, _MessageContainer


class MessageHandler:

    def __init__(self, regex: str):
        self.regex: Pattern = re.compile(regex)

    def __call__(self, method: Callable):
        handler = _MessageContainer()
        handler.method = method
        handler.regex = self.regex
        return handler


class ViewHandler:

    def __init__(self, state):
        self.state = state

    def _build_message_handler(self, cls, name: str) -> _MessageContainer:
        handler_message = _MessageContainer()
        handler_message.method = name
        handler_message.regex = cls.__dict__[name].regex
        return handler_message

    def _build_view_handler(self, cls) -> _ViewContainer:
        handler = _ViewContainer()
        handler.state = self.state
        instance_handler = cls()
        handler.cls = instance_handler
        handler.mcl = []
        return handler

    def _rollback_method(self, cls, name: str) -> None:
        setattr(cls, name, cls.__dict__[name].method)

    def __call__(self, cls):
        # init cls
        cls.state = self.state
        # init handler
        handler_view = self._build_view_handler(cls)
        for name in cls.__dict__.keys():
            if isinstance(cls.__dict__[name], _MessageContainer):
                handler_message = self._build_message_handler(cls, name)
                handler_view.mcl.append(handler_message)
                self._rollback_method(cls, name)
        VkBot._handlers[self.state] = handler_view
        return cls
