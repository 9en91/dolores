from dolores.views import View


class Consts:
    def __init__(self):
        self._state = None
        self._user_model = None
        self._views = None
        self._models = []

        self._database_config = None
        self._driver = None

        self._platform = None

        self._middleware = []

    def add_middleware(self, middleware):
        self._middleware.append(middleware)

    def get_middleware(self,):
        return self._middleware

    def add_view_in_chain(self, view: View):
        if self._views is None:
            self._views = view
        else:
            self._views.add_next(view)

    def get_views(self):
        return self._views

    def get_user_model(self):
        return self._user_model

    def add_model(self, model):
        self._models.append(model)

    def add_user_model(self, user_model):
        self._user_model = user_model

    def get_state(self):
        return self._state

    def set_state(self, state_model):
        self._state = state_model

    def get_driver(self):
        return self._driver

    def set_driver(self, driver):
        self._driver = driver

    def get_database_config(self):
        return self._database_config

    def set_database_config(self, database_config):
        self._database_config = database_config

    def get_platform(self):
        return self._platform

    def set_platform(self, platform):
        self._platform = platform


consts = Consts()
