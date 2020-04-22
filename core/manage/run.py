from typing import Any

from core.base import Application
from core.manage.abstract import AbstractCommand


class RunCommand(AbstractCommand):

    def handle(self, request: Any) -> None:
        if request == "run":
            print("RUN")
            bot = Application()
            # bot.polling()
        else:
            super().handle(request)
