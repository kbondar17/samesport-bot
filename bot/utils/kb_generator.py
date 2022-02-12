from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


from db.db_funs import repo

def generate_kb(entities, my_callback_data):

    buttons = []
    for e in entities:
        button = [InlineKeyboardButton(text='Название', callback_data=f'{e}#{callback}')]
        buttons.append(button)

    kb = InlineKeyboardMarkup(inline_keyboard=[buttons])
    return kb

# kb = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(
#             text='Название', callback_data='edit_name')],
#         [InlineKeyboardButton(
#             text='Описание', callback_data='edit_descr')],
#         [InlineKeyboardButton(
#             text='Распиcание', callback_data='edit_timetable')],
#         [InlineKeyboardButton(
#             text='< Отменить', callback_data='back_to_start')],

#     ]

# )
