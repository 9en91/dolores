from typing import List

from marshmallow import Schema, fields, post_load

from core.platforms.vk.types.message import Response, Message, ClientInfo, ObjectResponse


class MessageSchema(Schema):
    date: int = fields.Integer(data_key="date")
    from_id: int = fields.Integer(data_key="from_id")
    message_id: int = fields.Integer(data_key="id")
    out: int = fields.Integer(data_key="out")
    peer_id: int = fields.Integer(data_key="peer_id")
    text: str = fields.String(data_key="text")
    conversation_message_id: int = fields.Integer(data_key="conversation_message_id")
    fwd_messages: List = fields.List(fields.String, data_key="fwd_messages")
    important: bool = fields.Boolean(data_key="important")
    random_id: int = fields.Integer(data_key="random_id")
    attachments: List = fields.List(fields.String, data_key="attachments")
    is_hidden: bool = fields.Boolean(data_key="is_hidden")

    @post_load
    def make(self, data, **kwargs):
        return Message(**data)


class ClientInfoSchema(Schema):
    button_actions: List[str] = fields.List(fields.String, data_key="button_actions")
    keyboard: bool = fields.Boolean(data_key="keyboard")
    inline_keyboard: bool = fields.Boolean(data_key="inline_keyboard")
    lang_id: int = fields.Integer(data_key="lang_id")
    carousel: bool = fields.Boolean(allow_none=True)

    @post_load
    def make(self, data, **kwargs):
        return ClientInfo(**data)


class ObjectResponseSchema(Schema):
    message: MessageSchema = fields.Nested(MessageSchema(), data_key="message")
    client_info: ClientInfoSchema = fields.Nested(ClientInfoSchema(), data_key="client_info")

    @post_load
    def make(self, data, **kwargs):
        return ObjectResponse(**data)


class ResponseSchema(Schema):
    type_response: str = fields.String(data_key="type")
    object_response: ObjectResponseSchema = fields.Nested(ObjectResponseSchema(), data_key="object")
    group_id: int = fields.Integer(data_key="group_id")
    event_id: str = fields.String(data_key="event_id")

    @post_load
    def make(self, data, **kwargs):
        return Response(**data)
