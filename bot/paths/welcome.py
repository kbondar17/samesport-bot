from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext

from bot.loader import get_logger, dp
from bot.db.db_funs import wp_repo

from bot.my_states import My_states

logger = get_logger(f'my_log-{__name__}')


welcome_text =  'Здравствуйте, я чат-бот SameSport. Я помогаю поддерживать актуальность информации о спортивных секциях на портале SameSport'
main_menu = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='📝 Изменить данные секции'),
                                                KeyboardButton(text='❓ О боте')],
                                              ]
                                    )


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    # приветственное сообщение
    # если пользователь не авторизован - просим ввести логин/пароль

    user_id = message.from_user.id
    
    # check_if_authorized = wp_repo.check_if_authorized(user_id)
    check_if_authorized = True
    await message.answer(text=welcome_text)
    
    if not check_if_authorized:
        await My_states.typing_email.set()
        await message.answer(text='Давайте авторизуемся! Отправьте почту, с которой регистрировались на сайте samesport.ru 👇🏻')


@dp.message_handler(state=My_states.typing_email)
async def check_email(message: types.Message, state: FSMContext):
    email = message.text
    if email == 'samesport@mail.ru':
        await message.answer("Отлично! А теперь пароль")
        await My_states.typing_pass.set()
    
    else:
        await message.answer("Эта почта не подойдет. Попробуйте другую.")
    


@dp.callback_query_handler(text_contains='cancel', state='*')
async def back_to_start(call: types.CallbackQuery, state: FSMContext):
    await state.reset_state()
    await call.message.answer(text=welcome_text, reply_markup=main_menu)
