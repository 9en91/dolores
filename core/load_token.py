import os

from core.const import _BASE_DIR


@property
def bot_token() -> str:
    with open(os.path.join(_BASE_DIR, "token.txt")) as file:
        token = file.read()
    return token
