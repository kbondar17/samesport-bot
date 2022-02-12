from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher import FSMContext

from bot.loader import get_logger, dp
from bot.db.db_funs import repo

from bot.my_states import My_states

logger = get_logger(f'my_log-{__name__}')

kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text='Отменить', callback_data='cancel')],
    ]

)

text = '<b><u>Сейчас на сайте следующие данные:</u></b>\
        \n\n<b>Название:</b>\n\n{}\n\n\
<b>Описание:</b>\n\n{}\n\n\
<b>Распиcание:</b>\n\n{}'


@dp.callback_query_handler(text_contains='edit_name')
async def change(call: types.CallbackQuery):
    await My_states.typing_name.set()
    await call.message.answer('👇🏻 Отправь новое название сообщением! 👇🏻', reply_markup=kb)


@dp.callback_query_handler(text_contains='edit_descr')
async def change(call: types.CallbackQuery):
    await My_states.typing_descr.set()
    await call.message.answer('👇🏻 Отправь новое описание сообщением! 👇🏻', reply_markup=kb)


@dp.callback_query_handler(text_contains='edit_timetable')
async def change(call: types.CallbackQuery):
    await My_states.typing_timetable.set()
    await call.message.answer('👇🏻 Отправь новое расписание! 👇🏻', reply_markup=kb)


@dp.message_handler(state=My_states.typing_name)
async def get_text(message: types.Message, state: FSMContext):
    await state.reset_state()
    new_name = message.text
    repo.change_name(name=new_name, u_id=2)
    await message.answer('Поменяли название. Теперь вот так!')
    sec_info = repo.get_section_info()

    await message.answer(text.format(sec_info.name, sec_info.description, sec_info.timetable))


@dp.message_handler(state=My_states.typing_descr)
async def get_text(message: types.Message, state: FSMContext):
    await state.reset_state()
    new_name = message.text
    repo.change_description(description=new_name, u_id=2)
    await message.answer('Поменяли описание. Теперь вот так!')
    sec_info = repo.get_section_info()

    await message.answer(text.format(sec_info.name, sec_info.description, sec_info.timetable))


@dp.message_handler(state=My_states.typing_timetable)
async def get_text(message: types.Message, state: FSMContext):
    await state.reset_state()
    new_name = message.text
    repo.change_timetable(timetable=new_name, u_id=2)
    await message.answer('Поменяли расписание. Теперь вот так!')
    sec_info = repo.get_section_info()

    await message.answer(text.format(sec_info.name, sec_info.description, sec_info.timetable))
