from aiogram import types
from aiogram.contrib.middlewares.i18n import I18nMiddleware
from aiogram.types import ReplyKeyboardMarkup

from data.data import buttons


def menu(_: I18nMiddleware, **kwargs) -> types.ReplyKeyboardMarkup:
    keyboard: ReplyKeyboardMarkup = types.ReplyKeyboardMarkup(
        row_width=2,
        one_time_keyboard=False,
        resize_keyboard=True
    )
    for item in buttons['menu']:
        keyboard.insert(
            types.KeyboardButton(text=_(item, locale=kwargs.get('locale')))
        )

    return keyboard
