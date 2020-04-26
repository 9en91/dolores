class PlatformExceptions(Exception):
    pass

class NotSupportedPlatformException(PlatformExceptions):
    pass

class SoonPlatformException(PlatformExceptions):
    pass

class StateException(Exception):
    pass

class TooManyStateClasses(StateException):
    pass

class ModelsExceptions(Exception):
    pass

class TooManyUserModelsException(ModelsExceptions):
    pass

class NotExtensionUserModelException(ModelsExceptions):
    pass
