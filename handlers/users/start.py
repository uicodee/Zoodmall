from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram import md
from loader import dp
from utils import Zoodmall


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!\n")
