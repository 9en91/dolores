from core.decorators import ViewHandler, MessageHandler
from core.types import Message
from core.views import ViewSet
from tools.state import State


@ViewHandler(state=State.START)
class StartViewSet(ViewSet):

    @MessageHandler(regex="[Н,н]ачать")
    def func(self, event: Message) -> None:
        self.api.send_message(self.user, "Привет")

    @MessageHandler(regex="[П,п]ока")
    def fun(self, event: Message) -> None:
        self.api.send_message(self.user, "Пока")
