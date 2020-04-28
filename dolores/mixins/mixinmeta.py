import settings
from dolores.exceptions import NotSupportedPlatformException
from dolores.platforms import PLATFORMS


class PlatformMeta(type):

    def __new__(mcs, name, bases, namespace):
        if settings.PLATFORM == PLATFORMS.VK:
            _filter = lambda base: not base.__name__.startswith("Tg") and base.__name__.endswith("Mixin")
        elif settings.PLATFORM == PLATFORMS.TELEGRAM:
            _filter = lambda base: not base.__name__.startswith("Vk") and base.__name__.endswith("Mixin")
        else:
            raise NotSupportedPlatformException()
        bases = tuple(filter(_filter, bases))
        return super(PlatformMeta, mcs).__new__(type, name, bases, namespace)
