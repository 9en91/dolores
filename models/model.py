from dolores.decorators import Entity
from dolores.models import fields, Model


@Entity()
class Table(Model):
    name = fields.TextField(default="")

