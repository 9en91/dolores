from __future__ import annotations
from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):

    @abstractmethod
    def set_next(self, handler: Command) -> Command:
        pass

    @abstractmethod
    def handle(self, request) -> None:
        pass
