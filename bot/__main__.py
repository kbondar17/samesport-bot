from bot.loader import bot, dp, get_logger
from aiogram import executor
from bot.paths import dp


logger = get_logger(f'my_log-{__name__}')


if __name__ == '__main__':
    logger.debug('окей лестгоу')
    executor.start_polling(dp)
