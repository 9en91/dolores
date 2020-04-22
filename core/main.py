from core.base import Application
from core.utils import Utils
from core.view import View


def main():
    bot = Application()
    Utils.load_views()
    Utils.load_models()
    bot.polling()


if __name__ == '__main__':
    main()
