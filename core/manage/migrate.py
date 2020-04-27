from typing import Any, final

from core.models.migration import DatabaseMigrations
from core.manage.abstract import AbstractCommand


@final
class MigrateCommand(AbstractCommand):

    async def handle(self, request: Any) -> None:
        if request == "migrate":
            migrations = DatabaseMigrations()
            migrations.migrate()
        else:
            await super().handle(request)
