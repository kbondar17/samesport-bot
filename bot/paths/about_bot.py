import logging

from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from bot.loader import get_logger, dp
from bot.db.db_funs import repo

logger = get_logger(f'my_log-{__name__}')

@dp.message_handler(text_contains='О боте')
async def start(message: types.Message):
    await message.answer('Описание бота, контактная информация.')