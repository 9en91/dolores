from __future__ import annotations
from typing import List


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


class _MessageContainer:
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
