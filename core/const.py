from typing import Type


class Consts:
    from core.models import BaseUserModel
    from core.states import BaseState

    STATE: Type[BaseState] = BaseState
    views = {}
    user_model = BaseUserModel
    models = []
