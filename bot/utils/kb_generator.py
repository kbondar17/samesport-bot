from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



def generate_kb(entities, my_callback_data):

    buttons = []
    for e in entities:
        button = [InlineKeyboardButton(text=e, callback_data=f'{e}#{my_callback_data}')]
        buttons.append(button)

    kb = InlineKeyboardMarkup(inline_keyboard=[buttons])
    return kb
