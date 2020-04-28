import asyncio
from typing import Any

import settings
from dolores.platforms import PLATFORMS
from dolores.platforms.telegram.bot import TgBot
from dolores.platforms.vk.bot import VkBot
from dolores.manage.abstract import AbstractCommand


# @final
class RunCommand(AbstractCommand):

    async def handle(self, request: Any) -> None:
        if request == "run":
            try:
                if settings.PLATFORM == PLATFORMS.VK:
                    bot = VkBot()
                elif settings.PLATFORM == PLATFORMS.TELEGRAM:
                    bot = TgBot()
                else:
                    raise Exception
                await bot.polling()
            finally:
                await bot.api.close()
                await bot.close()
        else:
            await super().handle(request)
