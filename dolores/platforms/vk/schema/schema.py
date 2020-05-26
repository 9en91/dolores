from __future__ import annotations

from typing import List
from marshmallow import Schema, fields, post_load
from dolores.platforms.vk.types.message import (VkResponseType,
                                                VkMessageType,
                                                VkClientInfoType,
                                                VkObjectResponseType,
                                                VkAttachmentObjType)


class AttachmentObj(Schema):
    attach_type = fields.String(data_key="type")
    photo = fields.Dict(missing=True)
    audio = fields.Dict(missing=True)
    video = fields.Dict(missing=True)
    doc = fields.Dict(missing=True)
    wall = fields.Dict(missing=True)

    @post_load
    def make(self, data, **kwargs):
        return VkAttachmentObjType(**data)


class MessageSchema(Schema):
    date: int = fields.Integer(data_key="date")
    from_id: int = fields.Integer(data_key="from_id")
    message_id: int = fields.Integer(data_key="id")
    out: int = fields.Integer(data_key="out", missing=True)
    peer_id: int = fields.Integer(data_key="peer_id")
    text: str = fields.String(data_key="text")
    conversation_message_id: int = fields.Integer(data_key="conversation_message_id")
    fwd_messages: List = fields.List(fields.String, missing=True)
    important: bool = fields.Boolean(data_key="important", missing=True)
    random_id: int = fields.Integer(data_key="random_id", missing=True)
    attachments: List = fields.List(fields.Nested(AttachmentObj()), data_key="attachments", missing=True)
    is_hidden: bool = fields.Boolean(data_key="is_hidden", missing=True)
    reply_message: bool = fields.Nested('self', missing=True)
    geo = fields.Dict(missing=True)

    @post_load
    def make(self, data, **kwargs):
        return VkMessageType(**data)


class ClientInfoSchema(Schema):
    button_actions: List[str] = fields.List(fields.String, data_key="button_actions")
    keyboard: bool = fields.Boolean(data_key="keyboard",missing=True)
    inline_keyboard: bool = fields.Boolean(data_key="inline_keyboard", missing=True)
    lang_id: int = fields.Integer(data_key="lang_id")
    carousel: bool = fields.Boolean(missing=True)

    @post_load
    def make(self, data, **kwargs):
        return VkClientInfoType(**data)


class ObjectResponseSchema(Schema):
    message: MessageSchema = fields.Nested(MessageSchema(), data_key="message")
    client_info: ClientInfoSchema = fields.Nested(ClientInfoSchema(), data_key="client_info")

    @post_load
    def make(self, data, **kwargs):
        return VkObjectResponseType(**data)


class ResponseSchema(Schema):
    type_response: str = fields.String(data_key="type")
    object_response: ObjectResponseSchema = fields.Nested(ObjectResponseSchema(), data_key="object")
    group_id: int = fields.Integer(data_key="group_id")
    event_id: str = fields.String(data_key="event_id")


    @post_load
    def make(self, data, **kwargs):
        return VkResponseType(**data)
