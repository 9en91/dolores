from enum import unique, IntEnum, EnumMeta
from typing import final

from dolores.states import state


@unique
class _BaseState(IntEnum):
    START = state()


@final
class MetaState(EnumMeta):

    BASE = IntEnum

    @classmethod
    def __prepare__(mcs, name, bases):
        ret = super().__prepare__(name, (mcs.BASE,))

        for i in _BaseState:
            ret[i.name] = i.value  # noqa
        return ret

    def __new__(mcs, name, bases, namespace, **kwargs):
        return super().__new__(mcs, name, (mcs.BASE,), namespace)

    def __init__(cls, name, bases, namespace, **kwargs):
        super().__init__(name, (cls.BASE,), namespace)