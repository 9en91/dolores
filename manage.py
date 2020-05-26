import asyncio
import sys
from dolores.utils.loader import loader


async def main():
    if len(sys.argv) <= 1:
        raise Exception("missing argument")
    elif len(sys.argv) > 2:
        raise Exception("too many arguments")
    else:
        loader.load()

        from dolores.manage.migrate import MigrateCommand
        from dolores.manage.run import RunCommand

        run = RunCommand()
        migrate = MigrateCommand()
        run.set_next(migrate)
        await run.handle(sys.argv[1])


if __name__ == '__main__':
    asyncio.run(main())
