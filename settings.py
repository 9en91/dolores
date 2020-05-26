import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(BASE_DIR, "static")

TOKEN = "dsgnofdsgjf876t6r236rfe56wfdtsasaygd6q232h738w"
ID_BOT = 188183065

USER = "dolores.models.BaseUserModel"
STATE = "dolores.states.BaseState"

MIDDLEWARE = [
    "dolores.middleware.base.vk.VkHandleUpdateErrorMiddleware",
    "dolores.middleware.base.vk.VkUpdateServerMiddleware",
    "dolores.middleware.base.vk.VkMessageUpdateMiddleware",
    "dolores.middleware.base.vk.VkCastEventMiddleware",
    "dolores.middleware.base.vk.VkUserMiddleware",
    "dolores.middleware.base.vk.VkIsNotBannedUserMiddleware",
]

DATABASE = {
    "CONFIG": {
        "database": "predict_db",
        "user": "postgres",
        "password": "root",
        "host": "localhost",
        "port": 5432,
    },
    "DRIVER": "dolores.database.drivers.PostgresqlDatabase"
}

"""
Supported platform:
VK
TELEGRAM
DISCORD
"""
PLATFORM = "VK"
