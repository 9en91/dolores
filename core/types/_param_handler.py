from __future__ import annotations
from dataclasses import dataclass
from typing import Callable, List


class ViewContainer:

    __cls = None
    __state = None
    __mcl: List[MessageContainer] = None

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

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.__cls} [{self.__mcl}]"


class MessageContainer:
    __regex = None
    __method = None

    @property
    def regex(self):
        return self.__regex

    @regex.setter
    def regex(self, value):
        self.__regex = value

    @property
    def method(self):
        return self.__method

    @method.setter
    def method(self, value):
        self.__method = value

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.__regex} [{self.__method}]"


