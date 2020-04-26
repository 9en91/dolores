import logging
import time
import requests
import copy
import aiohttp
from vk_api import utils

import settings

logger = logging.getLogger("platform.vk")

class VkApi:

    RPS_DELAY = 0.34

    def __init__(self, token, api_version="5.92"):
        self.token = {'access_token': token}
        self.api_version = api_version
        self.http = requests.Session()
        self.http.headers.update({
            'User-agent': 'Mozilla/5.0 (Windows NT 6.1; rv:52.0) Gecko/20100101 Firefox/52.0'
        })
        self.last_request = 0.0

    def get_api(self):
        return VkApiMethod(self)


    def method(self, method, values=None):
        if values:
            values = copy.deepcopy(values)
        else:
            values = {}

        if "v" not in values:
            values["v"] = self.api_version

        values["access_token"] = self.token["access_token"]

        delay = self.RPS_DELAY - (time.time() - self.last_request)
        if delay > 0:
            time.sleep(delay)

        response = self.http.post(f"https://api.vk.com/method/{method}", values)
        self.last_request = time.time()

        if response.ok:
            response = response.json()
        else:
            raise Exception
        # if "error" in response:
        #     raise Exception
        return response


class VkApiMethod:

    def __init__(self, vk, method=None):
        self._vk = vk
        self._method = method

    def __getattr__(self, method):
        if self._method:
            method = f"{self._method}.{method}"

        return VkApiMethod(self._vk, method)

    def __call__(self, **kwargs):
        return self._vk.method(self._method, kwargs)

if __name__ == '__main__':
    vk = VkApi(token=settings.TOKEN)
    api = vk.get_api()
    api.messages.send(user_id=226507491,
                      random_id=utils.get_random_id(),
                      message="Тест? М?")