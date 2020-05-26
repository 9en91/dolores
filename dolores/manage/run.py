import asyncio
from typing import Any

import settings
from dolores.const import consts
from dolores.exceptions import NotSupportedPlatformException
from dolores.platforms import PLATFORMS
from dolores.platforms.telegram.bot import TgBot
from dolores.platforms.vk.bot import VkBot
from dolores.manage.abstract import AbstractCommand


# @final
class RunCommand(AbstractCommand):

    async def handle(self, request: Any) -> None:
        if request == "run":
            bot = None
            try:
                if consts.get_platform() == PLATFORMS.VK:
                    bot = VkBot()
                elif consts.get_platform() == PLATFORMS.TELEGRAM:
                    bot = TgBot()
                else:
                    raise NotSupportedPlatformException
                await bot.polling()
            finally:
                await bot.api.close()
                await bot.close()
        else:
            await super().handle(request)
