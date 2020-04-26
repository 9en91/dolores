from __future__ import annotations
from abc import ABCMeta
from typing import Final

from core.api import get_active_api


class ViewSet(metaclass=ABCMeta):

    def __init__(self):
        self.api: Final = get_active_api()
        self.user: Final = None


