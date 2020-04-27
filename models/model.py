from dolores.decorators import Entity
from dolores.models import fields, BaseUserModel, Model


@Entity.User
class UserModel(BaseUserModel):
    pass


@Entity
class ChatModel(Model):
    user = fields.TextField()

