import logging

from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from bot.loader import get_logger, dp
from bot.db.db_funs import repo
from bot.utils.kb_generator import generate_kb


logger = get_logger(f'my_log-{__name__}')

@dp.message_handler(text_contains='Изменить данные')
async def change(message: types.Message):
    # выбираем секции юзера
    # ! в разработке
    user_sections = ['Баскетбольная секция'] # айди секций
    kb = generate_kb(user_sections, my_callback_data='edit_choosen')
 
