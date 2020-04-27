from __future__ import annotations
import asyncio
import time
from abc import abstractmethod, ABCMeta
from typing import Dict
import aiohttp
import six

from vk_api.vk_api import VkApiMethod

from dolores.platforms.base.builder import BuilderApi


class AbstractAPI(metaclass=ABCMeta):
    RPS_DELAY = 0.34
    url: str = None

    def __init__(self, token: str, session: aiohttp.ClientSession):
        self.token = token
        self.last_request = 0.0
        if session:
            self.session = session
        else:
            self.session = aiohttp.ClientSession(headers={
                "User-agent":
                    "Mozilla/5.0 (Windows NT 6.1; rv:52.0) Gecko/20100101 Firefox/52.0"
            })

    @abstractmethod
    def _build_params_request(self, params: Dict) -> Dict:
        pass

    def build(self):
        return BuilderApi(self)

    async def method(self, method: str, params: Dict = None) -> Dict:
        params = self._build_params_request(params)
        delay = self.RPS_DELAY - (time.time() - self.last_request)
        if delay > 0.0:
            await asyncio.sleep(delay)
        response = await self.session.post(f"{self.url}{method}", data=params)
        self.last_request = time.time()
        return await response.json()

    def __del__(self):
        asyncio.create_task(self._close())

    async def _close(self):
        if not self.session.closed:
            await self.session.close()


