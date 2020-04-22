from __future__ import annotations
from typing import Any
from core.decorator import view
from core.view import View
from utils.state import State


@view(state=State.START)
class StartView(View):

    @view.message(regex="[Н,н]ачать")
    def func(self, event: Any) -> None:
        self.api.send_message(self.user.id, "Привет")

    @view.message(regex="[П,п]ока")
    def fun(self, event: Any) -> None:
        self.api.send_message(self.user.id, "Пока")
