from aiogram import types
from aiogram.contrib.middlewares.i18n import I18nMiddleware

from callback_datas import favourite_product


def operation_keyboard(_: I18nMiddleware, product_id: int) -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        types.InlineKeyboardButton(text=_('⭐️ Saqlash'), callback_data=favourite_product.new(product_id=product_id))
    )
    return keyboard