from typing import Any, final

from core.platforms.vk.vk_bot import VkBot
from core.manage.abstract import AbstractCommand


@final
class RunCommand(AbstractCommand):

    def handle(self, request: Any) -> None:
        if request == "run":
            bot = VkBot()
            bot.polling()
        else:
            super().handle(request)
