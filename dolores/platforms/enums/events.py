from enum import Enum


class VkMessageEvents(Enum):
    message_new = "message_new"
    message_reply = "message_reply"
    message_edit = "message_edit"
    message_allow = "message_allow"
    message_deny = "message_deny"

