import peewee
from core.database import Model as ModelBase
from core.const import Consts


class BaseUserModel(ModelBase):
    _state: int = peewee.IntegerField(column_name="state", default=int(Consts._STATE.START))
    _admin: bool = peewee.BooleanField(column_name="admin", default=False)

    @property
    def state(self) -> Consts._STATE:
        return Consts._STATE(self._state)

    @state.setter
    def state(self, state: Consts._STATE) -> None:
        self._state = int(state)

    @property
    def is_admin(self) -> bool:
        return self._admin

    @is_admin.setter
    def is_admin(self, value: bool) -> None:
        self._admin = value


