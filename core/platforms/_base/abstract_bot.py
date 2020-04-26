from abc import ABCMeta


class AbstractBot(metaclass=ABCMeta):

    def __init__(self):
        print("starting bot...")
        _handlers = {}
        self.__user_model = None
        self.__post_init()

    def __post_init(self):
        from core.const import _Consts
        self._handlers = _Consts._views
        self.__user_model = _Consts._user_model

    def _init_user(self, event):
        user, created = self.__user_model.get_or_create(id=event.message.from_id)
        return user
