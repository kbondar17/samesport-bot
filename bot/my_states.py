from aiogram.dispatcher.filters.state import StatesGroup, State


class My_states(StatesGroup):
    typing_email = State()
    typing_pass = State()
    
    
    typing_name = State()
    typing_descr = State()
    typing_timetable = State()
    typing_contacts = State()
    typing_adress = State()

    poll_how_many = State()
    poll_how_many_from_same = State()
    poll_feed_back = State()
    poll_end = State()
