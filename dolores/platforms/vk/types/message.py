from __future__ import annotations
from dataclasses import dataclass
from typing import List, Dict


@dataclass
class VkAttachmentObjType:
    attach_type: str
    doc: Dict
    photo: Dict
    audio: Dict
    video: Dict
    wall: Dict


@dataclass
class VkMessageType:
    date: int
    from_id: int
    message_id: int
    peer_id: int
    text: str
    conversation_message_id: int
    attachments: List[VkAttachmentObjType]
    out: int
    important: bool
    random_id: int
    fwd_messages: List[VkMessageType]
    is_hidden: bool
    reply_message: VkMessageType
    geo: Dict


@dataclass
class VkClientInfoType:
    button_actions: List[str]
    lang_id: int
    keyboard: bool
    inline_keyboard: bool
    carousel: bool


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




