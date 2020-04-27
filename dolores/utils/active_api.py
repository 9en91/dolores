import telebot

import settings
from dolores.exceptions import NotSupportedPlatformException
from dolores.platforms import PLATFORMS
from dolores.platforms.telegram.api import TgAPI
from dolores.platforms.vk.api import VkAPI


def get_active_api():
    if settings.PLATFORM == PLATFORMS.VK:
        api = VkAPI(token=settings.TOKEN)
    elif settings.PLATFORM.TELEGRAM:
        api = TgAPI(token=settings.TOKEN)
    else:
        raise NotSupportedPlatformException("Not supported")
    return api