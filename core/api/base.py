class BaseMixin:
    def _build_params_to_api(self, **kwargs):
        result = kwargs.copy()
        for x in kwargs:
            if kwargs[x] is None:
                del result[x]
        return result
