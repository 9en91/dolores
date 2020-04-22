from abc import abstractmethod
from core.manage.command import Command


class AbstractCommand(Command):
    _next_handler: Command = None

    def set_next(self, handler: Command) -> Command:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: str) -> None:
        if self._next_handler:
            self._next_handler.handle(request)
        else:
            print("incorrect command")
