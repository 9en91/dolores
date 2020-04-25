import re
from typing import Dict

from core.base import Application
from core.types._param_handler import ViewContainer, MessageContainer


class Message:  # noqa

    def __init__(self, regex):
        self.regex = regex

    def __call__(self, method):
        handler = MessageContainer()
        handler.method = method
        handler.regex = self.regex
        return handler
        # return {method.__name__: handler}

class View: # noqa

    def __init__(self, state):
        self.state = state

    def _build_message_handler(self, cls, name):
        handler_message = MessageContainer()
        handler_message.method = name
        handler_message.regex = re.compile(cls.__dict__[name].regex)
        return handler_message

    def _rollback_method(self, cls, name):
        setattr(cls, name, cls.__dict__[name].method)

    def __call__(self, cls):
        # init cls
        cls.state = self.state
        # init handler
        handler = ViewContainer()
        handler.state = self.state
        instance_handler = cls()
        handler.cls = instance_handler
        handler.mcl = []
        for name in cls.__dict__.keys():
            if isinstance(cls.__dict__[name], MessageContainer):
                handler_message = self._build_message_handler(cls, name)
                handler.mcl.append(handler_message)
                self._rollback_method(cls, name)
        Application._handlers[self.state] = handler
        return cls
