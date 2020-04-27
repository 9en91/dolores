from __future__ import annotations
from abc import abstractmethod, ABCMeta


class Command(metaclass=ABCMeta):

    @abstractmethod
    def set_next(self, handler: Command) -> Command:
        pass

    @abstractmethod
    async def handle(self, request) -> None:
        pass


class AbstractCommand(Command):
    _next_handler: Command = None

    def set_next(self, handler: Command) -> Command:
        self._next_handler = handler
        return handler

    @abstractmethod
    async def handle(self, request: str) -> None:
        if self._next_handler:
            await self._next_handler.handle(request)
        else:
            print("incorrect command")
