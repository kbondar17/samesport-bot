from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher import FSMContext

from bot.loader import get_logger, dp
from bot.db.db_funs import wp_repo

from bot.my_states import My_states



DEFUAULT_SECTION = 222

logger = get_logger(f'my_log-{__name__}')

from bot.paths.check_info import what_to_change_kb

kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text='Отменить', callback_data='cancel')],
    ]

)

text = '<b><u>Сейчас на сайте следующие данные:</u></b>\
        \n\n<b>Название:</b>\n\n{name}\n\n\
<b>Вид спорта:\n\n</b>{sport}\n\n\
<b>Описание:</b>\n\n{descr}\n\n\
<b>Распиcание:</b>\n\n{schedule}\n\n\
<b>Контакты:</b>\n\n{contacts}\n\n\
<b>Адрес:</b>\n\n{adress}'\



@dp.callback_query_handler(text_contains='edit_type')
async def change_type(call: types.CallbackQuery):
    kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text='Адаптивный', callback_data='type_changed#Адаптивный')],
        [InlineKeyboardButton(
            text='Инклюзивный', callback_data='type_changed#Инклюзивный')],
        [InlineKeyboardButton(
            text='< Отменить', callback_data='cancel')],

    ]
)
    await call.message.answer('Выберите тип', reply_markup=kb)


@dp.callback_query_handler(text_contains='edit_name')
async def ask_to_change_name(call: types.CallbackQuery):
    await My_states.typing_name.set()
    await call.message.answer('👇🏻 Отправьте новое название 👇🏻', reply_markup=kb)

@dp.callback_query_handler(text_contains='edit_contacts')
async def ask_to_change_contacts(call: types.CallbackQuery):
    await My_states.typing_contacts.set()
    await call.message.answer('👇🏻 Отправьте новые контакты 👇🏻', reply_markup=kb)


@dp.callback_query_handler(text_contains='edit_descr')
async def ask_to_change_descr(call: types.CallbackQuery):
    await My_states.typing_descr.set()
    await call.message.answer('👇🏻 Отправьте новое описание 👇🏻', reply_markup=kb)


@dp.callback_query_handler(text_contains='edit_timetable')
async def ask_to_change_timetable(call: types.CallbackQuery):
    await My_states.typing_timetable.set()
    await call.message.answer('👇🏻 Отправьте новое расписание 👇🏻', reply_markup=kb)

@dp.callback_query_handler(text_contains='edit_adress')
async def ask_to_change_adress(call: types.CallbackQuery):
    await My_states.typing_adress.set()
    await call.message.answer('👇🏻 Отправьте новый адрес 👇🏻', reply_markup=kb)


@dp.message_handler(state=My_states.typing_name)
async def change_name(message: types.Message, state: FSMContext):
    await state.reset_state()
    new_name = message.text
    wp_repo.change_name(new_name, uid=DEFUAULT_SECTION)

    await message.answer('Поменяли название. Теперь вот так:')
    sec_info = wp_repo.get_section_info(uid=222)
    
    await message.answer(text.format(name=sec_info['name'], descr=sec_info['description'],
                                contacts=sec_info['contacts'],  
                                schedule=sec_info['schedule'], sport=sec_info['sport'][0], adress=sec_info['adress']))
    
    await message.answer(text='Поменять что-нибудь еще?', reply_markup=what_to_change_kb)



@dp.message_handler(state=My_states.typing_descr)
async def change_descr(message: types.Message, state: FSMContext):
    await state.reset_state()
    new_name = message.text
    wp_repo.change_description(new_description=new_name, u_id=DEFUAULT_SECTION)
    await message.answer('Поменяли описание. Теперь вот так:')

    sec_info = wp_repo.get_section_info()

    await message.answer(text.format(sec_info.name, sec_info.description, sec_info.timetable))
    await message.answer(text='Поменять что-нибудь еще?', reply_markup=what_to_change_kb)


@dp.message_handler(state=My_states.typing_timetable)
async def change_timetable(message: types.Message, state: FSMContext):
    await state.reset_state()
    new_timetable = message.text
    

    wp_repo.change_timtable(new_timetable=new_timetable, u_id=DEFUAULT_SECTION)
    
    await message.answer('Поменяли расписание. Теперь вот так:')

    sec_info = wp_repo.get_section_info(uid=DEFUAULT_SECTION)

    await message.answer(text.format(name=sec_info['name'], descr=sec_info['description'],
                                    contacts=sec_info['contacts'],  
                                    schedule=sec_info['schedule'], sport=sec_info['sport'][0], adress=sec_info['adress']))
    
    await message.answer(text='Поменять что-нибудь еще?', reply_markup=what_to_change_kb)

@dp.message_handler(state=My_states.typing_contacts)
async def change_contacts(message: types.Message, state: FSMContext):
    await state.reset_state()
    new_contacts = message.text
    wp_repo.change_contacts(u_id=222, new_contacts=new_contacts)
    
    await message.answer('Поменяли контакты. Теперь вот так:')
    sec_info = wp_repo.get_section_info(uid=222)

    await message.answer(text.format(name=sec_info['name'], descr=sec_info['description'],
                                    contacts=sec_info['contacts'],  
                                    schedule=sec_info['schedule'], sport=sec_info['sport'][0], adress=sec_info['adress']))
    
    await message.answer(text='Поменять что-нибудь еще?', reply_markup=what_to_change_kb)





@dp.message_handler(state=My_states.typing_adress)
async def change_adress(message: types.Message, state: FSMContext):
    await state.reset_state()
    new_adress = message.text
    
    wp_repo.change_adress(new_adress, u_id=DEFUAULT_SECTION)
    
    await message.answer('Поменяли адрес. Теперь вот так:')
    #sec_info = repo.get_section_info()
    sec_info = wp_repo.get_section_info(uid=DEFUAULT_SECTION)

    await message.answer(text.format(name=sec_info['name'], descr=sec_info['description'],
                                    contacts=sec_info['contacts'],  
                                    schedule=sec_info['schedule'], sport=sec_info['sport'][0], adress=sec_info['adress']))

    await message.answer(text='Поменять что-нибудь еще?', reply_markup=what_to_change_kb)

