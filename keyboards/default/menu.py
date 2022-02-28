import typing
from aiogram import types
from aiogram.contrib.middlewares.i18n import I18nMiddleware
from aiogram.types import ReplyKeyboardMarkup


def menu(_: I18nMiddleware, **kwargs) -> types.ReplyKeyboardMarkup:
    keyboard: ReplyKeyboardMarkup = types.ReplyKeyboardMarkup(
        row_width=2,
        one_time_keyboard=False,
        resize_keyboard=True
    )
    data = ['🔍 Qidirish', '⭐️ Saqlangan', '⚙️ Sozlamalar']
    for item in data:
        keyboard.insert(
            types.KeyboardButton(text=_(item, locale=kwargs.get('locale')))
        )

    return keyboard
