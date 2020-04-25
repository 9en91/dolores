import os


def get_bot_token() -> str:
    path = os.path.abspath(os.curdir)
    with open(os.path.join(path, "token.txt")) as file:
        token = file.read()
    return token
