import asyncio
import sys


async def main():
    if len(sys.argv) <= 1:
        raise Exception("missing argument")
    elif len(sys.argv) > 2:
        raise Exception("too many arguments")
    else:
        from dolores.utils.loader import Loader

        Loader.load_state()
        Loader.load_models()
        Loader.load_views()

        from dolores.manage.migrate import MigrateCommand
        from dolores.manage.run import RunCommand

        run = RunCommand()
        migrate = MigrateCommand()
        run.set_next(migrate)
        await run.handle(sys.argv[1])


if __name__ == '__main__':
    asyncio.run(main())
