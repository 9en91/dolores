import peewee
from typing import final
from core.database import Model
from core.states import BaseState


@final
class DefaultUserModel(Model):
    state = peewee.IntegerField(default=BaseState.START)
    is_admin = peewee.BooleanField(default=False)
