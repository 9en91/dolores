from __future__ import annotations
from dataclasses import dataclass
from types import FunctionType
from typing import List, Pattern, Union, Type
from core.const import Consts
from core.views import View


@dataclass
class ViewContainer:
    cls: Type[View] = None
    state: Consts.STATE = None
    mcl: List[MessageContainer] = None


@dataclass
class MessageContainer:
    regex: Pattern
    method: Union[FunctionType, str]
    all: bool = False

    @classmethod
    def build(cls, other: MessageContainer):
        return cls(other.regex, other.method, other.all)


