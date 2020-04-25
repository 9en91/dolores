from typing import final

from core.states import state, BaseState


@final
class State(BaseState):
    SECOND = state()
