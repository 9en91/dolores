from typing import Tuple, Optional, Any

from dolores.const import consts
from dolores.middleware.abstract import Middleware
from dolores.platforms.enums.events import VkMessageEvents
from dolores.platforms.vk.types.message import VkMessageType, VkResponseType


class VkHandleUpdateErrorMiddleware(Middleware):

    def process(self, response):
        return response
        pass


class VkUpdateServerMiddleware(Middleware):

    def process(self, response):
        return response
        pass


class VkMessageUpdateMiddleware(Middleware):

    def process(self, update: VkResponseType) -> Optional[VkResponseType]:
        if update.type_response == str(VkMessageEvents.message_new):
            return update


class VkCastEventMiddleware(Middleware):

    def process(self, update: VkResponseType) -> Optional[VkMessageType]:
        return update.object_response.message


class VkUserMiddleware(Middleware):

    def process(self, event: VkMessageType) -> Tuple[VkMessageType, Any]:
        user, is_new = consts.get_user_model().get_or_create(id=event.from_id)
        return event, user


class VkIsNotBannedUserMiddleware(Middleware):

    def process(self,
                event: VkMessageType,
                user: Any) -> Optional[Tuple[VkMessageType, Any]]:
        if user.is_banned:
            return event, user
        else:
            return None
