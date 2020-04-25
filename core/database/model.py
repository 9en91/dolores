from peewee import Model as BaseModel
from core.database.__connector import DatabaseConnector


class Model(BaseModel):

    class Meta:
        database = DatabaseConnector.get_connection()
