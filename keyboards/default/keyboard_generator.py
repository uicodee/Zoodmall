from aiogram import types
from aiogram.types import ReplyKeyboardMarkup
from aiogram.contrib.middlewares.i18n import I18nMiddleware


def keyboard_generator(
        data: list,
        row_width: int,
        resize_keyboard: bool,
        one_time_keyboard: bool,
        _: I18nMiddleware,
        **kwargs
) -> types.ReplyKeyboardMarkup:
    keyboard: ReplyKeyboardMarkup = types.ReplyKeyboardMarkup(
        row_width=row_width,
        one_time_keyboard=one_time_keyboard,
        resize_keyboard=resize_keyboard
    )
    for item in data:
        keyboard.insert(
            types.KeyboardButton(text=_(item, locale=kwargs.get('locale')))
        )

    return keyboard
