from typing import List
from marshmallow import Schema, fields, post_load

from dolores.platforms.telegram.types.types import TgResponseType, TgChatType, TgFromType, TgMessageType,TgResultsType


class ChatSchema(Schema):
    chat_id: int = fields.Integer(data_key="id")
    first_name: str = fields.String(allow_none=True)
    last_name: str = fields.String(allow_none=True)
    username: int = fields.String(allow_none=True)
    type: str = fields.String()

    @post_load
    def make(self, data, **kwargs):
        return TgChatType(**data)


class FromSchema(Schema):
    from_id: int = fields.Integer(data_key="id")
    is_bot: bool = fields.Boolean()
    first_name: str = fields.String(allow_none=True)
    last_name: str = fields.String(allow_none=True)
    username: int = fields.String(allow_none=True)
    language_code: str = fields.String()

    @post_load
    def make(self, data, **kwargs):
        return TgFromType(**data)


class MessageSchema(Schema):
    message_id: int = fields.Integer()
    from_user: FromSchema = fields.Nested(FromSchema(), data_key="from")
    chat: ChatSchema = fields.Nested(ChatSchema())
    date: int = fields.Integer()
    text: str = fields.String()

    @post_load
    def make(self, data, **kwargs):
        return TgMessageType(**data)


class ResultsSchema(Schema):
    update_id: int = fields.Integer()
    message: MessageSchema = fields.Nested(MessageSchema())

    @post_load
    def make(self, data, **kwargs):
        return TgResultsType(**data)


class ResponseSchema(Schema):
    ok: str = fields.Boolean()
    result: List[ResultsSchema] = fields.List(fields.Nested(ResultsSchema()))

    @post_load
    def make(self, data, **kwargs):
        return TgResponseType(**data)
