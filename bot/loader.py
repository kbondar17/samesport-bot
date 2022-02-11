from dotenv import load_dotenv
import os
import logging
import logging.config
from yarl import URL

from aiogram import Bot, Dispatcher
from aiogram.types import ParseMode
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware


from config import TOKEN

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


def get_logger(name):
    logger = logging.getLogger(name)
    format = '%(filename)+13s %(name)s [ LINE:%(lineno)-4s] %(levelname)-8s [%(asctime)s] %(message)s'
    logger.setLevel(logging.DEBUG)
    sh = logging.StreamHandler()
    sh.setFormatter(logging.Formatter(format))
    sh.setLevel(logging.DEBUG)
    logger.addHandler(sh)
    return logger


logger = get_logger('my_logger:')
dp.middleware.setup(LoggingMiddleware(logger))
