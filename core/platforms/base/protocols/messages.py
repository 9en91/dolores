from abc import abstractmethod
from typing import Protocol, Any


class MessagesProtocol(Protocol):

    @abstractmethod
    async def send_message(self, user, text: str, keyboard: Any = None):
        pass