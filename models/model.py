import peewee

from core.database.default import DefaultUserModel
from core.database.model import Model
from core.utils import user_model, model


@user_model
class UserModel(DefaultUserModel):
    pass


@model
class ChatModel(Model):
    user = peewee.TextField()
