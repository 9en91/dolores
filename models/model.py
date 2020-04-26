from core.decorators import Entity
from core.models import fields, BaseUserModel, Model


@Entity.User
class UserModel(BaseUserModel):
    pass

@Entity
class ChatModel(Model):
    user = fields.TextField()

