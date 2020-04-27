from __future__ import annotations
import asyncio
import logging
import time
from typing import Dict

import aiohttp

from dolores.platforms.base.api import AbstractAPI


logger = logging.getLogger("platform.vk")


class VkAPI(AbstractAPI):

    url = "https://api.vk.com/method/"

    def __init__(self, token: str,
                 version: str = "5.103",
                 session: aiohttp.ClientSession = None):
        self.version = version
        super().__init__(token, session)

    def _build_params_request(self, params: Dict) -> Dict:
        if params:
            params = params.copy()
        else:
            params = {}
        if "v" not in params:
            params["v"] = self.version
        params["access_token"] = self.token
        return params

    async def method(self, method: str, params: Dict = None) -> Dict:
        params = self._build_params_request(params)
        delay = self.RPS_DELAY - (time.time() - self.last_request)
        if delay > 0.0:
            await asyncio.sleep(delay)
        response = await self.session.post(f"{self.url}{method}", data=params)
        self.last_request = time.time()
        return await response.json()
