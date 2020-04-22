class DatabaseConnector:
    @classmethod
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "__instance"):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        from settings import DATABASE
        self.__connect = DATABASE["DRIVER"](**DATABASE["CONFIG"])

    @staticmethod
    def get_connection():
        return DatabaseConnector().__connect
