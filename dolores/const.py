from typing import Type


class Consts:
    from dolores.models import BaseUserModel
    from dolores.states import BaseState

    STATE: Type[BaseState] = BaseState
    views = {}
    user_model = BaseUserModel
    models = []
