from dataclasses import dataclass
from typing import List


@dataclass
class Message:
    date: int
    from_id: int
    message_id: int
    out: int
    peer_id: int
    text: str
    conversation_message_id: int
    fwd_messages: List
    important: bool
    random_id: int
    attachments: List
    is_hidden: bool


@dataclass
class ClientInfo:
    button_actions: List[str]
    keyboard: bool
    inline_keyboard: bool
    lang_id: int
    carousel: bool


@dataclass
class ObjectResponse:
    message: Message
    client_info: ClientInfo


@dataclass
class Response:
    type_response: str
    object_response: ObjectResponse
    group_id: int
    event_id: str




