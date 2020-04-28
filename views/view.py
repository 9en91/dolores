from typing import Union

from dolores.decorators import ViewHandler, MessageHandler
from dolores.mixins.messages import MessagesMixin
from dolores.platforms.telegram.types.types import TgMessageType
from dolores.types import VkMessageType
from dolores.views import View
from tools.state import State


Message = Union[VkMessageType, TgMessageType]


@ViewHandler(state=State.START)
class StartView(View, MessagesMixin):

    @MessageHandler(regex="[П,п]ривет")
    async def hi(self, event: Message) -> None:
        await self.send_message(self.user, "Привет")

    @MessageHandler
    async def other(self, event: Message) -> None:
        await self.send_message(self.user, event.text)

