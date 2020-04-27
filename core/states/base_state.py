from __future__ import annotations
from core.states import MetaState


class BaseState(metaclass=MetaState):
    START: BaseState
    def __int__(self):
        return self.value
