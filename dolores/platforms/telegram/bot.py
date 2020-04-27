import asyncio
import itertools

import typing

from dolores.platforms.base.bot import AbstractBot
from dolores.platforms.telegram.api import TgAPI
from settings import TOKEN, ID_BOT


class TgBot(AbstractBot):

    def __init__(self, loop):
        super().__init__(loop)

        self.api = TgAPI(token=TOKEN, session=self.session)
        self.builder = self.api.build()
        self.group_id = ID_BOT

        self.limit = None
        self.timeout = 20
        self.offset = None

        self._close_waiter = loop.create_future()

        self.longpoll_schema = ...

    async def reset_webhook(self) -> bool:
        return await self.bot.delete_webhook()

    async def process_updates(self, updates, fast: typing.Optional[bool] = True):
        """
        Process list of updates

        :param updates:
        :param fast:
        :return:
        """
        if fast:
            tasks = []
            for update in updates:
                tasks.append(self.updates_handler.notify(update))
            return await asyncio.gather(*tasks)

    async def _process_polling_updates(self, updates, fast: typing.Optional[bool] = True):
        """
        Process updates received from long-polling.

        :param updates: list of updates.
        :param fast:
        """
        need_to_call = []
        for responses in itertools.chain.from_iterable(await self.process_updates(updates, fast)):
            for response in responses:
                if not isinstance(response, BaseResponse):
                    continue
                need_to_call.append(response.execute_response(self.bot))
        if need_to_call:
            try:
                await asyncio.gather(*need_to_call)
            except TelegramAPIError:
                log.exception('Cause exception while processing updates.')

    async def get_updates(self):
        params = dict(limit=self.limit, offset=self.offset, timeout=self.timeout)
        result = await self.api.method("getUpdates", params)
        return result

    async def polling(self, fast: typing.Optional[bool] = True):
        if self._polling:
            raise RuntimeError('Polling already started')

        # await self.reset_webhook()
        self._polling = True

        while self._polling:
            # try:
                # with self.bot.request_timeout(request_timeout):
            updates = await self.get_updates()
            # except asyncio.CancelledError:
            #     break
            # except:
            #     await asyncio.sleep(error_sleep)
            #     continue

            if updates:
                self.offset = updates[-1].update_id + 1

                self.loop.create_task(self._process_polling_updates(updates, fast))

            # if relax:
            #     await asyncio.sleep(self)

        # finally:
        #     self._close_waiter.set_result(None)