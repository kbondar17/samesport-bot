import logging
import asyncio

from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext

from bot.loader import get_logger, bot, dp
from bot.db.db_funs import wp_repo 
from bot.my_states import My_states

logger = get_logger(f'my_log-{__name__}')


async def start_poll():
    # сбор обратной связи от пользователей 
    await asyncio.sleep(2678400)

    kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Да, конечно',callback_data='poll#yes'),
    InlineKeyboardButton(text='В другой раз', callback_data='poll#no')  ]])
    await bot.send_message(text='Здравствуйте! Есть время ответить на два коротких вопроса? Вы нам очень поможите.', chat_id=283233169, reply_markup=kb)
    

@dp.callback_query_handler(text_contains='poll')
async def first_question(call: types.CallbackQuery):
    await call.message.answer(text='Сколько за прошедший месяц к вам обратилось новых людей? (отправьте цифру)')
    await My_states.poll_how_many.set()


@dp.message_handler(state=My_states.poll_how_many)
async def second_question(message: types.Message, state: FSMContext):
    if message.text != '0':    
        await message.answer(text='Сколько из них знают о сайте samesport.ru?')
    wp_repo.add_user_data(uid=1, number=message.text)
    await My_states.poll_how_many_from_same.set()
    

@dp.message_handler(state=My_states.poll_how_many_from_same)
async def final_question(message: types.Message, state: FSMContext):
 
    wp_repo.add_user_data_2(uid=1, number=message.text)
    await message.answer(text='Можете отправить комментарий на любую тему в сообщении')
    await My_states.poll_end.set()


@dp.message_handler(state=My_states.poll_end)
async def final_question(message: types.Message, state: FSMContext):
    await message.answer(text='Спасибо за обратную связь! Это очень помогает в работе 🙏🏻')
    await state.reset_state()



