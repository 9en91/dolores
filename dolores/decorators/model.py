from typing import final
from dolores.exceptions import NotExtensionUserModelException
from dolores.models import BaseUserModel

@final
class Entity:
    def __new__(cls, model):
        from dolores.const import Consts
        Consts.models.append(model)

    @final
    class User:
        using = False

        def __new__(cls, user_model):
            from dolores.const import Consts
            if not issubclass(user_model, BaseUserModel):
                raise NotExtensionUserModelException("wrong class inherited")
            Consts.user_model = user_model
            Entity.User.using = True
