from dataclasses import dataclass
from typing import List


@dataclass
class TgChatType:
    chat_id: int
    type: str
    first_name: str = None
    last_name: str = None
    username: int = None


@dataclass
class TgFromType:
    from_id: int
    is_bot: bool
    language_code: str
    first_name: str = None
    last_name: str = None
    username: int = None


@dataclass
class TgMessageType:
    message_id: int
    from_user: TgFromType
    chat: TgChatType
    date: int
    text: str


@dataclass
class TgResultsType:
    update_id: int
    message: TgMessageType


@dataclass
class TgResponseType:
    ok: str
    result: List[TgResultsType]
