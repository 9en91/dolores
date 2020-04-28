import peewee_async
from peewee import Model as BaseModel
from dolores.models.connector import DatabaseConnector
import peewee


class Model(BaseModel):
    __objects = peewee_async.Manager(DatabaseConnector.get_connection())

    @classmethod
    async def get_or_create(cls, defaults=None, **kwargs):
        return await Model.__objects.get_or_create(cls, defaults=None, **kwargs)

    class Meta:
        database = DatabaseConnector.get_connection()


class BaseUserModel(Model):
    _state: int = peewee.IntegerField(column_name="state", default=1)
    _admin: bool = peewee.BooleanField(column_name="admin", default=False)

    @property
    def state(self):
        from dolores.const import Consts
        return Consts.STATE(self._state)

    @state.setter
    def state(self, state) -> None:
        self._state = int(state)

    @property
    def is_admin(self) -> bool:
        return self._admin

    @is_admin.setter
    def is_admin(self, value: bool) -> None:
        self._admin = value
