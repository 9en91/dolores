from __future__ import annotations
from typing import Any
from core.decorator import View, Message
from core.viewset import ViewSet
from utils.state import State


@View(state=State.START)
class StartViewSet(ViewSet):

    @Message(regex="[Н,н]ачать")
    def func(self, event: Any) -> None:
        self.api.send_message(self.user, "Привет")

    @Message(regex="[П,п]ока")
    def fun(self, event: Any) -> None:
        self.api.send_message(self.user, "Пока")
