import os
from typing import Type, TypeVar, List
from core.database.default import DefaultUserModel
from core.database.model import Model as DbModel


_UserModel = TypeVar("_UserModel", bound=DefaultUserModel)
_Model = TypeVar("_Model", bound=DbModel)


_USER_MODEL: Type[_UserModel] = DefaultUserModel

_MODEL_FOR_MIGRATE: List[Type[_Model]] = []

_BASE_DIR = os.path.abspath(os.curdir)


_TOKEN = TOKEN
_ID_BOT = ID_BOT

_DATABASE = DATABASE

_STATE = STATE


