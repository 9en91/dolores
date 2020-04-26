from __future__ import annotations
from dataclasses import dataclass
from types import FunctionType
from typing import List, Pattern, Union, Type
from core.const import Consts
from core.views import ViewSet


@dataclass
class _ViewContainer:
    cls: Type[ViewSet] = None
    state: Consts._STATE = None
    mcl: List[_MessageContainer] = None


@dataclass
class _MessageContainer:
    regex: Pattern
    method: Union[FunctionType, str]
    all: bool = False

    @classmethod
    def build(cls, other: _MessageContainer):
        return cls(other.regex, other.method, other.all)


