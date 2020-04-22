from core.base import Application
from core.types._param_handler import _Handler # noqa


class view: # noqa
    class message: # noqa

        def __init__(self, regex):
            self.regex = regex

        def __call__(self, method):
            return _Handler(self.regex, method)

    def __init__(self, state):
        self.state = state

    def __call__(self, cls):
        cls.state = self.state
        self.__create(cls)
        return cls

    def __create(self, cls):  # noqa
        for i in cls.__dict__.keys():
            if isinstance(cls.__dict__[i], _Handler):
                if cls.state in Application._handlers: # noqa
                    Application._handlers[cls.state].append(cls.__dict__[i]) # noqa
                else:
                    Application._handlers[cls.state] = [cls.__dict__[i]] # noqa
