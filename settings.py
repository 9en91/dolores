import os
from typing import Dict
from peewee import PostgresqlDatabase
from core.utils.load_token import get_bot_token


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TOKEN: str = get_bot_token()
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
