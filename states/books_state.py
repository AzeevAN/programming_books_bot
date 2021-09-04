from aiogram.dispatcher.filters.state import StatesGroup, State


class StateBook(StatesGroup):
    name = State()
    year = State()
    author = State()
    language = State()
    book_language = State()
    file_book = State()
