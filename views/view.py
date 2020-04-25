from core.decorators import ViewHandler, MessageHandler
from core.types import Message
from core.views import ViewSet
from tools.state import State


@ViewHandler(state=State.START)
class StartViewSet(ViewSet):

    @MessageHandler(regex="[Н,н]ачать")
    def start(self, event: Message) -> None:
        self.api.send_message(self.user, "Ой, ты что-то начал")

    @MessageHandler(regex="[П,п]ока")
    def bye(self, event: Message) -> None:
        self.api.send_message(self.user, "Ну пока")

    @MessageHandler(regex="[П,п]ривет")
    def hi(self, event: Message) -> None:
        self.api.send_message(self.user, "Привет")
