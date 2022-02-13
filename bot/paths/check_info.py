import logging

from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher import FSMContext

from bot.loader import get_logger, dp
from bot.db.db_funs import wp_repo
from bot.my_states import My_states

logger = get_logger(f'my_log-{__name__}')

what_to_change_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text='Название', callback_data='edit_name')],
        [InlineKeyboardButton(
            text='Описание', callback_data='edit_descr')],
        [InlineKeyboardButton(
            text='Распиcание', callback_data='edit_timetable')],
        [InlineKeyboardButton(
            text='Контакты', callback_data='edit_contacts')],
        [InlineKeyboardButton(
            text='Адрес', callback_data='edit_adress')],
        [InlineKeyboardButton(
            text='< Отменить', callback_data='cancel')],

    ]

) 


text = '<b><u>Сейчас на сайте следующие данные:</u></b>\
        \n\n<b>Название:</b>\n\n{name}\n\n\
<b>Вид спорта:\n\n</b>{sport}\n\n\
<b>Описание:</b>\n\n{descr}\n\n\
<b>Распиcание:</b>\n\n{schedule}\n\n\
<b>Контакты:</b>\n\n{contacts}\n\n\
<b>Адрес:</b>\n\n{adress}'\



# юзер, который только что аутентифицировался
@dp.message_handler(state=My_states.typing_pass)
async def check_email(message: types.Message, state: FSMContext):

    passwods = message.text

    if passwods == 'password':
        await state.reset_state()
        await message.answer('Все верно. Вы авторизованы.')
        wp_repo.set_user_is_authorized(message.from_user.id)
        sec_info = wp_repo.get_section_info(uid=222)

        await message.answer(text.format(name=sec_info['name'], descr=sec_info['description'],
                                    contacts=sec_info['contacts'],  
                                    schedule=sec_info['schedule'], sport=sec_info['sport'][0], adress=sec_info['adress']))

        await message.answer(text='Что меняем?', reply_markup=what_to_change_kb)
        await message.delete()

    else:
        await message.answer('Неправильный пароль. Попробуйте другой.')


# аутентифицированный юзер
@dp.message_handler(text_contains='Изменить данные')
async def change(message: types.Message):
   
    # показываем текущие данные, предлагаем выбрать, что изменить
    check_if_authorized = True
    if check_if_authorized:
        sec_info = wp_repo.get_section_info(uid=222)

        
        sec_info = wp_repo.get_section_info(uid=222)

        await message.answer(text.format(name=sec_info['name'], descr=sec_info['description'],
                                    contacts=sec_info['contacts'],  
                                    schedule=sec_info['schedule'], sport=sec_info['sport'][0], adress=sec_info['adress']))

        await message.answer(text='Что меняем?', reply_markup=what_to_change_kb)
    
    else:
        await message.answer(text='Вы не авторизованы. Пришлите почту, на которую зарегистрирован аккаунт на Samesport.ru')
        await My_states.typing_email.set()





