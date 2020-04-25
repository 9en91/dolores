from typing import Any, final

from core.database.migration import migrate
from core.manage.abstract import AbstractCommand


@final
class MigrateCommand(AbstractCommand):

    def handle(self, request: Any) -> None:
        if request == "migrate":
            migrate()
        else:
            super().handle(request)
