from core.states import BaseState, state
from core.database.model import Model
from core.decorators.model import Entity
from core.database import fields


@Entity.User
class UserModel(Model):
    pass


@Entity
class ChatModel(Model):
    user = fields.TextField()

