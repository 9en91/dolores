from core.decorators import ViewHandler, MessageHandler
from core.types import VkMessagesMixin, VkMessageType
from core.views import View
from tools.state import State


@ViewHandler(state=State.START)
class StartView(View, VkMessagesMixin):

    @MessageHandler(regex="[П,п]ривет")
    async def hi(self, event: VkMessageType) -> None:
        await self.send_message(self.user, "Привет")


    @MessageHandler
    async def other(self, event: VkMessageType) -> None:
        await self.send_message(self.user, event.text)

