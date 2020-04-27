from typing import final
from dolores.states import state, BaseState


@final
class State(BaseState):
    SECOND = state()
