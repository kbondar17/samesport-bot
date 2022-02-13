from bot.loader import bot, dp, get_logger
from aiogram import executor
from bot.paths import dp
import asyncio

logger = get_logger(f'my_log-{__name__}')

from bot.paths.user_poll.start_poll import start_poll



if __name__ == '__main__':
    logger.debug('окей лестгоу')

    loop = asyncio.get_event_loop()
    loop.create_task(start_poll())
    
    
    executor.start_polling(dp)
