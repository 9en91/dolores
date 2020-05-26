from dolores.decorators import Controller
from dolores.platforms.enums.content import VkContent
from dolores.platforms.vk.mixins.message import VkMessagesMixin
from dolores.types.message_type import MessagesType
from dolores.views import View
from dolores.states import BaseState


@Controller(state=BaseState.START,
            event=MessagesType.USER,
            content=[VkContent.text],
            text="[Н,н]ачать")
class StartView(View, VkMessagesMixin):

    async def handle(self, event, user, *args, **kwargs):
        answer: str = "текс"
        await self.send_message(user=user,
                                text=answer)

