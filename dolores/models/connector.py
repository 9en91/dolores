# from typing import final
from dolores.const import consts
from settings import DATABASE


# @final
class DatabaseConnector:
    @classmethod
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "__instance"):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        consts.get_driver()
        self.__connect = consts.get_driver()(**DATABASE["CONFIG"])

    @staticmethod
    def get_connection():
        return DatabaseConnector().__connect
