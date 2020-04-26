import sys


def main():
    if len(sys.argv) <= 1:
        raise Exception("missing argument")
    elif len(sys.argv) > 2:
        raise Exception("too many arguments")
    else:
        from core.utils._loader import _Loader

        _Loader.load_state()
        _Loader.load_models()
        _Loader.load_views()

        from core.manage.migrate import MigrateCommand
        from core.manage.run import RunCommand

        run = RunCommand()
        migrate = MigrateCommand()
        run.set_next(migrate)
        run.handle(sys.argv[1])


if __name__ == '__main__':
    main()


