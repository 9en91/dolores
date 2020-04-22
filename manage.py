from core.database.migration import migrate
from core.main import main as bot_run
import sys


def main():
    try:
        command = sys.argv[1]
        if command == "run":
            bot_run()
        elif command == "migrate":
            migrate()
        else:
            print("don't know")
    except IndexError:
        print("please add command")


if __name__ == '__main__':
    main()


