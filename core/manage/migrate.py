from typing import Any, final

from core.database.migration import DatabaseMigrations
from core.manage.abstract import AbstractCommand


@final
class MigrateCommand(AbstractCommand):

    def handle(self, request: Any) -> None:
        if request == "migrate":
            migrations = DatabaseMigrations()
            migrations.migrate()
        else:
            super().handle(request)
