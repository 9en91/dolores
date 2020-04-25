from enum import auto

from core.states.basestate import MetaState


class BaseState(metaclass=MetaState):
    pass


class state(int, auto):
    pass
