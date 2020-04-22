from typing import Any

from core.manage.abstract import AbstractCommand


class MigrateCommand(AbstractCommand):

    def handle(self, request: Any) -> None:
        if request == "migrate":
            # migrate()
            print("MIGRATE")
        else:
            super().handle(request)