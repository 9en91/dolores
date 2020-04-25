from __future__ import annotations

import re
from dataclasses import dataclass
from types import FunctionType
from typing import List, Pattern, Union


class _ViewContainer:

    __cls = None
    __state = None
    __mcl: List[_MessageContainer] = None

    @property
    def cls(self):
        return self.__cls

    @cls.setter
    def cls(self, value):
        self.__cls = value

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        self.__state = value

    @property
    def mcl(self):
        return self.__mcl

    @mcl.setter
    def mcl(self, value):
        self.__mcl = value


@dataclass
class _MessageContainer:
    regex: Pattern
    method: Union[FunctionType, str]
    all: bool = False

    @classmethod
    def build(cls, other: _MessageContainer):
        return cls(other.regex, other.method, other.all)


