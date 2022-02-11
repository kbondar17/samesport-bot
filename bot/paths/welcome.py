import logging

from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from bot.loader import get_logger, dp
from bot.db.db_funs import repo

logger = get_logger(f'my_log-{__name__}')


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    # первое сообщение

    main_menu = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='📝 Изменить данные секции')],
                                              ]
                                    )

    user_id = message.from_user.id
    user_name = message.from_user.username
    repo.add_user(user_id, user_name=user_name)
    # repo.set_username(uid=user_id, name=user_name)
    await message.answer('Привет! Тут можно изменить данные о вашей секции на сайте samesport.ru! Нажми "изменить данные в меню" ', reply_markup=main_menu)
    logger.debug('юзер %s нажал на старт', message.from_user.id)
#    await message.answer(text=welcome_text, reply_markup=main_menu)
