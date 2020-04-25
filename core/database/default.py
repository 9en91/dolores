import peewee

from core.database import Model
from core.states import BaseState


class DefaultUserModel(Model):
    state = peewee.IntegerField(default=BaseState.START)
    is_admin = peewee.BooleanField(default=False)

    is_new_user = None
