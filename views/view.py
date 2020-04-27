from vk_api import utils

from core.decorators import ViewHandler, MessageHandler
from core.platforms.vk.types.message import VkMessageType
from core.views import ViewSet
from tools.state import State


@ViewHandler(state=State.START)
class StartViewSet(ViewSet):

    @MessageHandler(regex="[П,п]ривет")
    async def hi(self, event: VkMessageType) -> None:
        await self.api.messages.send(user_id=self.user.id,
                                     random_id=utils.get_random_id(),
                                     message="Привет")

    @MessageHandler
    async def other(self, event: VkMessageType) -> None:
        await self.api.messages.send(user_id=self.user.id,
                                     random_id=utils.get_random_id(),
                                     message="Не понимаю")
