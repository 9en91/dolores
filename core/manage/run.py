import asyncio
from typing import Any, final

from core.platforms.vk.bot import VkBot
from core.manage.abstract import AbstractCommand


@final
class RunCommand(AbstractCommand):

    async def handle(self, request: Any) -> None:
        if request == "run":
            loop = asyncio.get_event_loop()
            bot = VkBot(loop)
            await bot.polling()
        else:
            await super().handle(request)
