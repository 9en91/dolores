from __future__ import annotations
from abc import abstractmethod, ABCMeta
from typing import Dict
import aiohttp
from dolores.platforms.base.builder import BuilderApi


class AbstractAPI(metaclass=ABCMeta):
    RPS_DELAY = 0.05
    url: str = None

    def __init__(self, token: str, session: aiohttp.ClientSession = None):
        self.token = token
        self.last_request = 0.0
        if session:
            self.session = session
        else:
            self.session = aiohttp.ClientSession(headers={
                "User-agent":
                    "Mozilla/5.0 (Windows NT 6.1; rv:52.0) Gecko/20100101 Firefox/52.0"
            })

    def build(self):
        return BuilderApi(self)

    @abstractmethod
    async def method(self, method: str, params: Dict = None) -> Dict:
        pass

    async def close(self):
        await self.session.close()


