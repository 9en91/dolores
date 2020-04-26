import peewee
from core.database import Model as ModelBase
from core.states import BaseState


class BaseUserModel(ModelBase):
    _state: int = peewee.IntegerField(column_name="state", default=int(BaseState.START))
    _admin: bool = peewee.BooleanField(column_name="admin", default=False)

    @property
    def state(self) -> BaseState:
        return BaseState(self._state)

    @state.setter
    def state(self, state: BaseState) -> None:
        self._state = int(state)

    @property
    def is_admin(self) -> bool:
        return self._admin

    @is_admin.setter
    def is_admin(self, value: bool) -> None:
        self._admin = value

    class Meta:
        table = "users"


