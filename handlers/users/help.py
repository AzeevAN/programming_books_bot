from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Начать диалог",
            "/help - Получить справку",
            '/new_book - Добавить новую книгу',
            '/list_of_books - Список доступных книг')
    
    await message.answer("\n".join(text))
