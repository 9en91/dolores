from typing import Callable


class _Handler:
    regex: str
    fun: Callable

    def __init__(self, regex, fun):
        self.regex = regex
        self.fun = fun
