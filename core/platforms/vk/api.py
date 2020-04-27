from __future__ import annotations
import asyncio
import logging
import time
from typing import Dict

import aiohttp

from core.platforms.base.api import AbstractAPI


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
