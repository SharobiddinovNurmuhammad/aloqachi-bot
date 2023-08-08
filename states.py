from aiogram.dispatcher.filters.state import State, StatesGroup

class Connection(StatesGroup):
    answer_msg = State()
   