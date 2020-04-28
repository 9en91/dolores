import re
from types import FunctionType
from typing import Pattern, Callable, Union
from dolores.utils.view_container import ViewContainer, MessageContainer


# @final
class MessageHandler:

    def __new__(cls, regex: Union[FunctionType, str]):
        if not isinstance(regex, FunctionType):
            return super(MessageHandler, cls).__new__(cls)
        else:
            return MessageContainer(re.compile(".*"), regex, True)

    def __init__(self, *, regex: str = ".*"):
        self.regex: Pattern = re.compile(regex)

    def __call__(self, method: Callable):
        return MessageContainer(self.regex, method, False)


# @final
class ViewHandler:
    _handlers = {}

    def __init__(self, state):
        self.state = int(state)

    def _build_message_handler(self, cls, name: str) -> MessageContainer:
        handler_message = MessageContainer(cls.__dict__[name].regex, name, cls.__dict__[name].all)
        return handler_message

    def _build_view_handler(self, cls) -> ViewContainer:
        handler = ViewContainer()
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
            if isinstance(cls.__dict__[name], MessageContainer):
                handler_message = self._build_message_handler(cls, name)
                handler_view.mcl.append(handler_message)
                self._rollback_method(cls, name)
        handler_view.mcl = sorted(handler_view.mcl, key=lambda x: x.all)
        from dolores.const import Consts
        Consts.views[self.state] = handler_view
        return cls