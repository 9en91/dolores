from typing import final
from core.exceptions import TooManyUserModelsException, NotExtensionUserModelException
from core.models import BaseUserModel

@final
class Entity:
    models = []

    def __new__(cls, model):

        Entity.models.append(model)

    @final
    class User:
        _using = False
        model = None

        def __new__(cls, user_model):
            from core.const import _Consts
            if not issubclass(user_model, BaseUserModel):
                raise NotExtensionUserModelException("wrong class inherited")
            if not Entity.User._using:
                _Consts._user_model = user_model
                Entity.User._using = True
            else:
                raise TooManyUserModelsException("too many user model exception")
