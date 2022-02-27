from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from filters import is_user
from data.data import welcome
from keyboards.inline import language_markup


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(
        text=welcome,
        reply_markup=language_markup()
    )


@dp.message_handler(is_user(), CommandStart())
async def bot_start(message: types.Message, language: str):
    print(language)
    await message.answer(f"Привет, {message.from_user.full_name}!\n")


