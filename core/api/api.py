from vk_api import VkApi
from vk_api.vk_api import VkApiMethod

import settings
from core.api.messages import MessagesMixin


class VkAPI(MessagesMixin):
    api: VkApiMethod = VkApi(token=settings.TOKEN).get_api()
