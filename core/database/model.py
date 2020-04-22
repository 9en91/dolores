from peewee import Model as BaseModel


class Model(BaseModel):

    class Meta:
        from core.database.__connector import DatabaseConnector
        database = DatabaseConnector.get_connection()
