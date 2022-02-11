import logging

from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from bot.loader import get_logger, dp
from bot.db.db_funs import repo

logger = get_logger(f'my_log-{__name__}')

kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text='Название', callback_data='edit_name')],
        [InlineKeyboardButton(
            text='Описание', callback_data='edit_descr')],
        [InlineKeyboardButton(
            text='Распиcание', callback_data='edit_timetable')],
        [InlineKeyboardButton(
            text='< Отменить', callback_data='back_to_start')],

    ]

)


@dp.message_handler(text_contains='Изменить данные')
async def change(message: types.Message):
    # показываем текущие данные, предлагаем выбрать, что изменить

    sec_info = repo.get_section_info()

    text = f'<b><u>Сейчас на сайте следующие данные:</u></b>\
        \n\n<b>Название:</b>\n\n{sec_info.name}\n\n\
<b>Описание:</b>\n\n{sec_info.description}\n\n\
<b>Распиcание:</b>\n\n{sec_info.timetable}'

    await message.answer(text=text)
    await message.answer(text='Что меняем?', reply_markup=kb)
