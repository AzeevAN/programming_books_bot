from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.inline.callback_datas import callback_language
from keyboards.inline.state_book_buttons import language_books_programming, button_programming_books
from loader import dp, bot


@dp.message_handler(Command("list_of_books"), state=None)
async def enter_test(message: types.Message):
    await message.answer("Выберите язык программирования", reply_markup=language_books_programming)


@dp.callback_query_handler(callback_language.filter(), state=None)
async def set_language_of_programming_book(call: types.CallbackQuery, callback_data: dict):
    await call.answer(cache_time=20)

    language_name = callback_data['language_name']

    await bot.edit_message_text(text=f"Книги по языку {language_name}",
                                reply_markup=button_programming_books(language_name),
                                chat_id=call.from_user.id,
                                message_id=call.message.message_id
                                )



