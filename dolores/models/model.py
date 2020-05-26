import peewee_async
from peewee import Model as BaseModel

from dolores.const import consts
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
    _banned: bool = peewee.BooleanField(column_name="banned", default=False)

    @property
    def state(self):
        return consts.get_state()(self._state)

    @state.setter
    def state(self, state) -> None:
        self._state = int(state)

    @property
    def is_admin(self) -> bool:
        return self._admin

    @is_admin.setter
    def is_admin(self, value: bool) -> None:
        self._admin = value

    @property
    def is_banned(self) -> bool:
        return self._banned

    @is_banned.setter
    def is_banned(self, value: bool) -> None:
        self._banned = value
