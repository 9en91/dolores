class BuilderApi:

    def __init__(self, api, method=None):
        self._api = api
        self._method = method

    def __getattr__(self, method: str):
        if self._method:
            method = f"{self._method}.{method}"
        self._method = method
        return BuilderApi(self._api, method)

    async def __call__(self, **kwargs):
        return await self._api.method(self._method, kwargs)


class VkApiMethod(object):

    def __init__(self, vk, method=None):
        self._vk = vk
        self._method = method

    def __getattr__(self, method):
        return VkApiMethod(
            self._vk,
            (self._method + '.' if self._method else '') + method
        )

    def __call__(self, **kwargs):
        return self._vk.method(self._method, kwargs)