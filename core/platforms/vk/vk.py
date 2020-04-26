from __future__ import annotations
import asyncio
import logging
import time
from typing import Dict
import aiohttp


logger = logging.getLogger("platform.vk")


class VkApi:
    RPS_DELAY = 0.34

    def __init__(self, token: str,
                 api_version: str = "5.103"):

        self.token = token
        self.api_version = api_version
        self.last_request = 0.0
        self.session = aiohttp.ClientSession(headers={
            "User-agent":
                "Mozilla/5.0 (Windows NT 6.1; rv:52.0) Gecko/20100101 Firefox/52.0"
        })

    def _build_params_request(self, params: Dict) -> Dict:
        if params:
            params = params.copy()
        else:
            params = {}
        if "v" not in params:
            params["v"] = self.api_version
        params["access_token"] = self.token
        return params

    async def method(self, method: str, params: Dict = None) -> Dict:
        params = self._build_params_request(params)
        delay = self.RPS_DELAY - (time.time() - self.last_request)
        if delay > 0.0:
            await asyncio.sleep(delay)
        response = await self.session.post(f"https://api.vk.com/method/{method}", data=params)
        self.last_request = time.time()
        return await response.json()

    def __getattr__(self, method: str) -> VkApi:
        if self._method:
            method = f"{self._method}.{method}"
        self._method = method
        return self

    async def __call__(self, **kwargs):
        return await self.method(self._method, kwargs)

    def __del__(self):
        asyncio.create_task(self._close())

    async def _close(self):
        if not self.session.closed:
            await self.session.close()


