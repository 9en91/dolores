from __future__ import annotations
from abc import ABCMeta
from typing import Final
from core.utils.active_api import get_active_api


class View(metaclass=ABCMeta):

    def __init__(self):
        self.api: Final = get_active_api().build()
        self.user: Final = None


