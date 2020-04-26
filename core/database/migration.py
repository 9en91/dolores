from core.database.__connector import DatabaseConnector
from core.database.default import BaseUserModel
from core.decorators import Entity
from core.utils._loader import _Loader


class DatabaseMigrations:

    def __post_init(self):
        if Entity.User._using:
            self.model_for_migrations.append(Entity.User.model)
        else:
            self.model_for_migrations.append(BaseUserModel)
        self.model_for_migrations += Entity.models


    def __init__(self):
        self.model_for_migrations = []
        _Loader.load_models()
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
