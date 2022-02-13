from aiogram import types


from bot.loader import get_logger, dp


logger = get_logger(f'my_log-{__name__}')

@dp.message_handler(text_contains='О боте')
async def start(message: types.Message):
    await message.answer('я чат-бот SameSport. Я помогаю поддерживать актуальность информации о спортивных секциях на портале SameSport.\
         По вопросам и предложения пишите @ovkhokhr')