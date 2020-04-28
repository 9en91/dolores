from __future__ import annotations
from abc import ABCMeta
# from typing import Final
from dolores.utils.active_api import get_active_api


class View(metaclass=ABCMeta):

    def __init__(self, api):
        self.api = api
        self.user = None
        super().__init__()
