class BuilderMixin:
    def _build(self, **kwargs):
        result = kwargs.copy()
        for x in kwargs:
            if kwargs[x] is None:
                del result[x]
        return result
