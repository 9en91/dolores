import telebot

import settings
from core.exceptions import NotSupportedPlatformException
from core.platforms import PLATFORMS
from core.platforms.vk.api import VkAPI


def get_active_api():
    if settings.PLATFORM == PLATFORMS.VK:
        api = VkAPI(token=settings.TOKEN)
    elif settings.PLATFORM.TELEGRAM:
        api = telebot.TeleBot(token=settings.TOKEN)
    else:
        raise NotSupportedPlatformException("Not supported")
    return api