from core.models.connector import DatabaseConnector
from core.models import BaseUserModel
from core.decorators import Entity


class DatabaseMigrations:

    def __post_init(self):
        from core.const import Consts
        if Entity.User.using:
            self.model_for_migrations.append(Consts.user_model)
        else:
            self.model_for_migrations.append(BaseUserModel)
        self.model_for_migrations += Consts.models


    def __init__(self):
        self.model_for_migrations = []
        self.__post_init()

    def migrate(self):
        print("Start migration:")
        connect = DatabaseConnector.get_connection()
        connect.connect()
        connect.drop_tables(self.model_for_migrations, cascade=True)
        connect.create_tables(self.model_for_migrations)
        connect.close()
        for index, i in enumerate(self.model_for_migrations):
            print(f"{index + 1}. {i.__name__} - competed")
        print("\nAll migrate competed")
