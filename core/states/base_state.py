from __future__ import annotations
from enum import IntEnum, auto, EnumMeta, unique
from typing import final


@final
class state(int, auto):
    pass


@unique
class _BaseState(IntEnum):
    START = state()


@final
class MetaState(EnumMeta):
    START: BaseState
    __BASE = IntEnum

    @classmethod
    def __prepare__(mcs, name, bases):
        ret = super().__prepare__(name, (mcs.__BASE,))

        for i in _BaseState:
            ret[i.name] = i.value  # noqa
        return ret

    def __new__(mcs, name, bases, namespace, **kwargs):
        return super().__new__(mcs, name, (mcs.__BASE,), namespace)

    def __init__(cls, name, bases, namespace, **kwargs):
        super().__init__(name, (cls.__BASE,), namespace)


class BaseState(metaclass=MetaState):
    pass



