class BuilderApi:

    def __init__(self, api, method=None):
        self._api = api
        self._method = method

    def __getattr__(self, method: str):
        return BuilderApi(self._api, (self._method + '.' if self._method else '') + method)

    async def __call__(self, **kwargs):
        response = await self._api.method(self._method, kwargs)
        self._method = None
        return response
