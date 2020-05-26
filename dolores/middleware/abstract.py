from abc import ABCMeta, abstractmethod
from typing import Any


class Middleware(metaclass=ABCMeta):
    @abstractmethod
    def process(self, *args, **kwargs) -> Any:
        pass
