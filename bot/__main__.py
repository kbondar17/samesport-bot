import asyncio

from bot.loader import bot, dp, get_logger
from aiogram import executor
from bot.paths import dp


logger = get_logger(f'my_log-{__name__}')


if __name__ == '__main__':

    # loop = asyncio.get_event_loop()
    # loop.create_task(notificator())

    # asyncio.run(notificator())

    # при старте асинхронно загрузить фотки ! .

    logger.debug('окей лестгоу')
    executor.start_polling(dp)
