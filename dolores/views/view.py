from __future__ import annotations
from abc import ABCMeta
# from typing import Final
from dolores.utils.active_api import get_active_api


class View:

    def __init__(self):
        self.api = get_active_api().build()
        self.user = None
        super().__init__()
