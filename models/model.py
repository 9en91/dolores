from core.database import Model
from core.decorators import Entity
from core.database import fields


@Entity.User
class UserModel(Model):
    pass


@Entity
class ChatModel(Model):
    user = fields.TextField()

