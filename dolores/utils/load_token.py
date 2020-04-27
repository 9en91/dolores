import os


def get_bot_token(path) -> str:
    with open(os.path.join(path, "token.txt")) as file:
        token = file.read()
    return token
