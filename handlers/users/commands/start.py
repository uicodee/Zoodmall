from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.data import welcome
from filters import is_user
from keyboards.inline import language_markup
from keyboards.default import menu
from loader import dp, _


@dp.message_handler(is_user(), CommandStart())
async def bot_start(message: types.Message) -> None:
    await message.answer(
        text=_("Assalomu Alaykum, xush kelibsiz!"),
        reply_markup=menu(_)
    )


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(
        text=welcome,
        reply_markup=language_markup()
    )





