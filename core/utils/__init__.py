import random


def get_random_id() -> int:
    return random.getrandbits(31) * random.choice([-1, 1])
