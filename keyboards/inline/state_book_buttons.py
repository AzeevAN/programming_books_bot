from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_datas import callback_language, callback_books

# Кнопки выбора перевода книги
from utils.db_api.sqlite3_db import select_all_books_witch_language_programming

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


def button_programming_books(language_name):
    # Кнопка выбора книг программирования
    books_programming = InlineKeyboardMarkup(row_width=1)

    data = select_all_books_witch_language_programming(language_name)

    total_count_button = 7
    count = 1
    for item in data:
        programing_button = InlineKeyboardButton(
            text=item[1], callback_data=callback_books.new(
                id=item[0]
            )
        )
        books_programming.insert(programing_button)
        count += 1
        if total_count_button == count:
            break

    return books_programming

    # books_programming = InlineKeyboardMarkup(
    #     inline_keyboard=[
    #         [
    #             InlineKeyboardButton(text='Python', callback_data=callback_language.new(
    #                 language_name='Python'
    #             )),
    #             InlineKeyboardButton(text='1C (1S)', callback_data=callback_language.new(
    #                 language_name='1C (1S)'
    #             ))
    #         ]
    #     ]
    # )

