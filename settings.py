import os
from peewee import PostgresqlDatabase
from core.load_token import bot_token


TOKEN = bot_token
ID_BOT = 188183065

DATABASE = {
    "CONFIG": {
        "database": "postgres",
        "user": "postgres",
        "password": "root",
        "host": "localhost",
        "port": 5432,
    },
    "DRIVER": PostgresqlDatabase
}

# BASE_DIR = os.path.abspath(os.curdir)
