import logging
import uuid

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text

from data.config import ADMINS
from keyboards.inline.callback_datas import callback_language
from keyboards.inline.state_book_buttons import language_books, language_books_programming
from loader import dp, bot
from states.books_state import StateBook
from utils.db_api import sqlite3_db


@dp.message_handler(Command("new_book"), state=None)
async def enter_test(message: types.Message):
    await message.answer("Добавление новой книги.\n"
                         "Для отмены введите команду /reset.\n"
                         "Пункт №1-6. \n\n"
                         "Укажите название книги")

    await StateBook.first()


@dp.message_handler(state='*', commands='reset')
@dp.message_handler(Text(equals='reset', ignore_case=True), state='*')
async def enter_test(message: types.Message, state: FSMContext):

    data = await state.get_data()
    name = data.get("name")

    if name is None:
        return

    logging.info('Отмена состояния машины')

    await state.reset_state()

    await message.reply('Данные добавления новой книги сброшены.')


@dp.message_handler(state=StateBook.name)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(name=answer)

    await message.answer("Пункт №2-6. \n\n"
                         f"Укажите год издания книги '{answer}'\n\n")

    await StateBook.next()


@dp.message_handler(state=StateBook.year)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(year=answer)

    data = await state.get_data()
    name = data.get("name")

    await message.answer("Пункт №3-6. \n\n"
                         f"Укажите автора(ов) книги '{name}'\n\n")

    await StateBook.next()


@dp.message_handler(state=StateBook.author)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(author=answer)

    data = await state.get_data()
    name = data.get("name")

    await message.answer("Пункт №4-6. \n\n"
                         f"Выберите язык программирования книги '{name}'",
                         reply_markup=language_books_programming)

    await StateBook.next()


@dp.callback_query_handler(callback_language.filter(), state=StateBook.language)
async def answer_q1(call: types.CallbackQuery, state: FSMContext, callback_data: dict):
    await call.answer(cache_time=10)

    answer = callback_data['language_name']
    await state.update_data(language=answer)

    data = await state.get_data()
    name = data.get("name")

    await bot.edit_message_text(text=
                                "Пункт №5-6. \n\n"
                                f"Выберите язык перевода книги '{name}'", reply_markup=language_books,
                                chat_id=call.from_user.id, message_id=call.message.message_id
                                )

    await StateBook.next()


@dp.callback_query_handler(callback_language.filter(), state=StateBook.book_language)
async def answer_q1(call: types.CallbackQuery, state: FSMContext, callback_data: dict):
    await call.answer(cache_time=10)

    answer = callback_data['language_name']
    await state.update_data(book_language=answer)

    data = await state.get_data()
    name = data.get("name")

    await bot.edit_message_text(text=
                                "Пункт №6-6. \n\n"
                                f"Пришлите мне файл книги '{name}'",
                                chat_id=call.from_user.id, message_id=call.message.message_id
                                )

    await StateBook.next()


@dp.message_handler(state=StateBook.file_book, content_types=types.ContentTypes.DOCUMENT)
async def bot_echo_all(message: types.Message, state: FSMContext):

    data = await state.get_data()
    name = data.get("name")

    await state.finish()

    uid_book = uuid.uuid4().hex

    active_book = False
    for admin in ADMINS:
        if admin == str(message.from_user.id):
            active_book = True

    data_book = (
        uid_book,
        name,
        data.get("author"),
        data.get("year"),
        data.get("language"),
        data.get("book_language"),
        active_book)

    res_add_book = sqlite3_db.create_books(data_book)
    res_add_book_address = False
    if res_add_book:
        book_address = [(
            message.document.file_unique_id,
            message.document.mime_type,
            message.document.file_id,
            uid_book,
            message.document.file_name,
            message.document.file_size)
        ]
        res_add_book_address = sqlite3_db.create_books_address(book_address)

    if res_add_book_address and res_add_book:
        text_message = f"Благодарю \n\nКнига '{name}' успешно добавлена на модерацию"
        if active_book:
            file_book = await bot.get_file(message.document.file_id)
            file_path = file_book.file_path
            await bot.download_file(file_path, 'books/' + message.document.file_unique_id + '_' + message.document.file_name)
    else:
        text_message = f'Не удалось добавить новую книжку {name}. Очень жаль :('

    await message.answer(text_message)

