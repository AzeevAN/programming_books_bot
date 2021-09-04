from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_datas import callback_language


# Кнопки выбора перевода книги
language_books = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='EN', callback_data=callback_language.new(
                language_name='EN'
            )),
            InlineKeyboardButton(text='RU', callback_data=callback_language.new(
                language_name='RU'
            ))
        ]
    ]
)

# Кнопка выбора языков программирования
language_books_programming = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Python', callback_data=callback_language.new(
                language_name='Python'
            )),
            InlineKeyboardButton(text='1C (1S)', callback_data=callback_language.new(
                language_name='1C (1S)'
            ))
        ]
    ]
)
