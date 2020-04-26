from core.database import Model
from core.decorators import Entity
from core.database import fields
from core.models import BaseUserModel


@Entity.User
class UserModel(BaseUserModel):
    pass

@Entity
class ChatModel(Model):
    user = fields.TextField()

