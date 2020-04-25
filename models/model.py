from core.basestate import BaseState, state
from core.database.model import Model
from core.decorators.model import Entity
from core.database.fields import field


@Entity.User
class UserModel(Model):
    pass


@Entity
class ChatModel(Model):
    user = field.TextField()

