from vk_api import VkApi

from core.exceptions import SoonPlatformException, NotSupportedPlatformException
from core.platforms import PLATFORMS
import settings
import telebot


def get_active_api():
    if settings.PLATFORM == PLATFORMS.VK:
        api = VkApi(token=settings.TOKEN).get_api()
    elif settings.PLATFORM.TELEGRAM:
        api = telebot.TeleBot(token=settings.TOKEN)
    else:
        raise NotSupportedPlatformException("Not supported")
    return api
