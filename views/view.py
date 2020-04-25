from core.decorators import ViewHandler, MessageHandler
from core.types import Message
from core.views import ViewSet
from tools.state import State


@ViewHandler(state=State.START)
class StartViewSet(ViewSet):

    @MessageHandler(regex="[Н,н]ачать")
    def start(self, event: Message) -> None:
        self.api.messages.send(self.user.id, "Ой, ты что-то начал")

    @MessageHandler(regex="[П,п]ривет")
    def hi(self, event: Message) -> None:
        self.api.messages.send(self.user.id, "Привет")

    @MessageHandler
    def bye(self, event: Message) -> None:
        self.api.messages.send(user_id=self.user.id,
                               message="Не понимаю")
