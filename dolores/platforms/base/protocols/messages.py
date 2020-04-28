from abc import abstractmethod
from typing import Any


class MessagesProtocol:

    @abstractmethod
    async def send_message(self, user, text: str, keyboard: Any = None) -> Any:
        pass