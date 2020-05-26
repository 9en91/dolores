import re
from types import FunctionType
from typing import Pattern, Callable, Union, List, Type

from dolores.const import consts
from dolores.platforms.enums.content import VkContent
from dolores.utils.view_container import ViewContainer, MessageContainer


# @final
# class MessageHandler:
#
#     # def __new__(cls, regex: Union[FunctionType, str]):
#     #     if not isinstance(regex, FunctionType):
#     #         return super(MessageHandler, cls).__new__(cls)
#     #     else:
#     #         return MessageContainer(re.compile(".*"), regex, True)
#
#     def __init__(self, *, regex: str = ".*", content: List = None):
#         self.regex: Pattern = re.compile(regex)
#         if content is None:
#             content = [VkContent.text]
#         self.content = content
#
#     def __call__(self, method: Callable):
#         return MessageContainer(self.regex, self.content, method, False)


# @final
from dolores.views import View


class Controller:

    def __init__(self, state, event, text: str, content: List):
        self.state = state
        self.event = event
        self.text = text
        self.content = content

    def __call__(self, cls: Type[View]):
        obj_view = cls()
        obj_view.set_event(self.event)
        obj_view.set_content(self.content)
        obj_view.set_text(self.text)
        obj_view.set_state(self.state)
        consts.add_view_in_chain(obj_view)

    # def _build_message_handler(self, cls, name: str) -> MessageContainer:
    #     handler_message = MessageContainer(cls.__dict__[name].regex, cls.__dict__[name].content, name, cls.__dict__[name].all)
    #     return handler_message
    #
    # def _build_view_handler(self, cls) -> ViewContainer:
    #     handler = ViewContainer()
    #     handler.state = self.state
    #     instance_handler = cls(None)
    #     handler.cls = instance_handler
    #     handler.mcl = []
    #     return handler
    #
    # def _rollback_method(self, cls, name: str) -> None:
    #     setattr(cls, name, cls.__dict__[name].method)
    #
    # def __call__(self, cls):
    #     # init cls
    #     cls.state = self.state
    #     # init handler
    #     handler_view = self._build_view_handler(cls)
    #     for name in cls.__dict__.keys():
    #         if isinstance(cls.__dict__[name], MessageContainer):
    #             handler_message = self._build_message_handler(cls, name)
    #             handler_view.mcl.append(handler_message)
    #             self._rollback_method(cls, name)
    #     handler_view.mcl = sorted(handler_view.mcl, key=lambda x: x.all)
    #     from dolores.const import Consts
    #     Consts.views[self.state] = handler_view
    #     return cls
