from dataclasses import dataclass
from typing import List


@dataclass
class VkMessageType:
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
class VkClientInfoType:
    button_actions: List[str]
    lang_id: int
    keyboard: bool = None
    inline_keyboard: bool = None
    carousel: bool = None


@dataclass
class VkObjectResponseType:
    message: VkMessageType
    client_info: VkClientInfoType


@dataclass
class VkResponseType:
    type_response: str
    object_response: VkObjectResponseType
    group_id: int
    event_id: str




