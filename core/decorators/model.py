from typing import final
from core.exceptions import TooManyUserModelsException, NotExtensionUserModelException
from core.models import BaseUserModel

@final
class Entity:
    def __new__(cls, model):
        from core.const import Consts
        Consts.models.append(model)

    @final
    class User:
        using = False

        def __new__(cls, user_model):
            from core.const import Consts
            if not issubclass(user_model, BaseUserModel):
                raise NotExtensionUserModelException("wrong class inherited")
            if not Entity.User.using:
                Consts.user_model = user_model
                Entity.User.using = True
            else:
                raise TooManyUserModelsException("too many user model exception")
