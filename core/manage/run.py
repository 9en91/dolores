from typing import Any

from core.platforms.vk.vk_bot import VkBot
from core.manage.abstract import AbstractCommand


class RunCommand(AbstractCommand):

    def handle(self, request: Any) -> None:
        if request == "run":
            print("RUN")
            bot = VkBot()
            bot.polling()
        else:
            super().handle(request)
