import os
from typing import Dict
from peewee import PostgresqlDatabase
from core.load_token import bot_token


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TOKEN: str = bot_token(BASE_DIR)
ID_BOT: int = 188183065

DATABASE: Dict = {
    "CONFIG": {
        "database": "postgres",
        "user": "postgres",
        "password": "root",
        "host": "localhost",
        "port": 5432,
    },
    "DRIVER": PostgresqlDatabase
}

