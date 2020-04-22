from core.const import _MODEL_FOR_MIGRATE
from core.database.__connector import DatabaseConnector
from core.database.default import DefaultUserModel


def migrate():
    print("Start migration:")
    _MODEL_FOR_MIGRATE.append(DefaultUserModel)
    connect = DatabaseConnector.get_connection()
    connect.connect()
    connect.drop_tables(_MODEL_FOR_MIGRATE, cascade=True)
    connect.create_tables(_MODEL_FOR_MIGRATE)
    connect.close()
    for index, i in enumerate(_MODEL_FOR_MIGRATE):
        print(f"{index + 1}. {i.__name__} - competed")
    print("\nAll migrate competed")
