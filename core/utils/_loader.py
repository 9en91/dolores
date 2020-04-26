import os
import glob
import importlib.util
from typing import final

from settings import BASE_DIR


@final
class _Loader:
    _path_views = os.path.join(BASE_DIR, "views")
    _path_models = os.path.join(BASE_DIR, "models")

    @staticmethod
    def load_views():
        for i, x, y in os.walk(_Loader._path_views):
            for path_view in glob.glob(f"{i}/*.py"):
                view = importlib.util.spec_from_file_location("views", path_view)
                view_module = importlib.util.module_from_spec(view)
                view.loader.exec_module(view_module)

    @staticmethod
    def load_models():
        for i, x, y in os.walk(_Loader._path_models):
            for path in glob.glob(f"{i}/*.py"):
                file = importlib.util.spec_from_file_location("models", path)
                module = importlib.util.module_from_spec(file)
                file.loader.exec_module(module)

    @staticmethod
    def load_state():
        try:
            from settings import STATE, BASE_DIR
        except ImportError:
            return
        from core.states._base_state import BaseState

        spl_path = STATE.split(".")
        name_cls = spl_path[-1]
        path_to_state = os.path.join(BASE_DIR, *spl_path[:-1])
        path = glob.glob(f"{path_to_state}.py")[0]
        file = importlib.util.spec_from_file_location("state", path)
        module = importlib.util.module_from_spec(file)
        file.loader.exec_module(module)
        state_cls = module.__dict__.get(name_cls, BaseState)
        from core.const import _Consts
        _Consts._STATE = state_cls
