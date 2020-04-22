import os
import glob
import sys
import importlib.util
from settings import BASE_DIR


class Utils:
    _path_views = os.path.join(BASE_DIR, "views")
    _path_models = os.path.join(BASE_DIR, "models")

    @staticmethod
    def load_views():
        for i, x, y in os.walk(Utils._path_views):
            for path_view in glob.glob(f"{i}/*[V, v]iew.py"):
                view = importlib.util.spec_from_file_location("views", path_view)
                view_module = importlib.util.module_from_spec(view)
                view.loader.exec_module(view_module)

    @staticmethod
    def load_models():
        for i, x, y in os.walk(Utils._path_models):
            for path in glob.glob(f"{i}/*.py"):
                file = importlib.util.spec_from_file_location("models", path)
                module = importlib.util.module_from_spec(file)
                file.loader.exec_module(module)

    @staticmethod
    def load_settings():
        for i, x, y in os.walk(Utils._path_models):
            for path in glob.glob(f"{i}/*.py"):
                file = importlib.util.spec_from_file_location("models", path)
                module = importlib.util.module_from_spec(file)
                file.loader.exec_module(module)


def user_model(cls):
    # from core.const import _USER_MODEL
    # global USER_MODEL
    # USER_MODEL = cls
    ...

def model(cls):
    # from core.const import _MODEL_FOR_MIGRATE
    # global MODEL_FOR_MIGRATE
    # _MODEL_FOR_MIGRATE.append(cls)
    ...


