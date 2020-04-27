import asyncio
import time
from typing import Dict
from dolores.platforms.base.api import AbstractAPI


class TgAPI(AbstractAPI):

    url = "https://api.telegram.org/bot{}/{}"

    async def method(self, method: str, params: Dict = None) -> Dict:
        delay = self.RPS_DELAY - (time.time() - self.last_request)
        if delay > 0.0:
            await asyncio.sleep(delay)
        response = await self.session.post(self.url.format(self.token, method), data=params)
        self.last_request = time.time()
        return await response.json()