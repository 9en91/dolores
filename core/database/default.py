import peewee

from core.database.model import Model
from core.basestate import BaseState


class DefaultUserModel(Model):
    state = peewee.IntegerField(default=BaseState.START)

    is_new_user = None
