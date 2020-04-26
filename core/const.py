from typing import Type


class _Consts:
    from core.models import BaseUserModel
    from core.states import BaseState

    _STATE: Type[BaseState] = BaseState
    _views = {}
    _user_model = BaseUserModel
    _models = []