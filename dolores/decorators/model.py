
from dolores.const import consts


class Entity:
    def __init__(self, abstract=None):
        self.abstract = abstract

    def __call__(self, cls):
        consts.add_model(cls)

    class User:
        def __init__(self):
            pass

        def __call__(self, cls):
            consts.add_user_model(cls)
