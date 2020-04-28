import os
from dolores.platforms import PLATFORMS
from dolores.utils.load_token import get_bot_token
import peewee_async

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

PLATFORM = PLATFORMS.VK
TOKEN = get_bot_token(BASE_DIR)
ID_BOT = 188183065

DATABASE = {
    "CONFIG": {
        "database": "postgres",
        "user": "postgres",
        "password": "root",
        "host": "localhost",
        "port": 5432,
    },
    "DRIVER": peewee_async.PostgresqlDatabase
}

STATE = "tools.state.State"
