from aiogram import types
from callback_datas import language
from data.data import languages


def language_markup() -> types.InlineKeyboardMarkup:
    keyboard: types.InlineKeyboardMarkup = types.InlineKeyboardMarkup(row_width=2)
    for language_name, language_code in languages.items():
        keyboard.insert(
            types.InlineKeyboardButton(text=language_name, callback_data=language.new(language_code=language_code))
        )
    return keyboard
