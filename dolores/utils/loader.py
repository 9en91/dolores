import os
import glob
import importlib.util
from typing import Type, Any
import settings
from dolores.const import consts
from dolores.platforms import PLATFORMS
from settings import BASE_DIR


class __Loader:
    _path_views = os.path.join(BASE_DIR, "views")
    _path_models = os.path.join(BASE_DIR, "models")

    def import_class_by_name(self, path: str) -> Type[Any]:
        components = path.split(".")
        module = importlib.import_module(".".join(components[:-1]))
        imported_class = getattr(module, components[-1])
        return imported_class

    def load_views(self):
        for i, x, y in os.walk(self._path_views):
            for path_view in glob.glob(f"{i}/*.py"):
                view = importlib.util.spec_from_file_location("views", path_view)
                view_module = importlib.util.module_from_spec(view)
                view.loader.exec_module(view_module)

    def load_models(self):
        for i, x, y in os.walk(self._path_models):
            for path in glob.glob(f"{i}/*.py"):
                file = importlib.util.spec_from_file_location("models", path)
                module = importlib.util.module_from_spec(file)
                file.loader.exec_module(module)

    def load_state(self):
        stated_class = self.import_class_by_name(settings.STATE)
        consts.set_state(stated_class)

    def load_database(self):
        stated_class = self.import_class_by_name(settings.DATABASE["DRIVER"])
        consts.set_driver(stated_class)

    def load_database_config(self):
        consts.set_database_config(settings.DATABASE)

    def load_platform(self):
        consts.set_platform(PLATFORMS[settings.PLATFORM])

    def load_middleware(self):
        for path_middleware in settings.MIDDLEWARE:
            stated_class = self.import_class_by_name(path_middleware)
            consts.add_middleware(stated_class)

    def load(self):
        self.load_database()
        self.load_models()
        self.load_state()
        self.load_views()
        self.load_database_config()
        self.load_platform()
        self.load_middleware()


loader = __Loader()
