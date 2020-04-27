from typing import Any

from dolores.models.migration import DatabaseMigrations
from dolores.manage.abstract import AbstractCommand


# @final
class MigrateCommand(AbstractCommand):

    async def handle(self, request: Any) -> None:
        if request == "migrate":
            migrations = DatabaseMigrations()
            migrations.migrate()
        else:
            await super().handle(request)
