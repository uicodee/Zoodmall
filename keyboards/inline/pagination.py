from aiogram import types
import typing
from callback_datas import select, paginator


def pagination(data: typing.List[typing.Dict], max_pages: int, current_page: int):
    keyboard = types.InlineKeyboardMarkup(row_width=5)
    for item in data:
        for i, j in item.items():
            keyboard.insert(
                types.InlineKeyboardButton(text=i, callback_data=select.new(product_id=j))
            )
    print(current_page)
    if current_page == max_pages:
        keyboard.add(
            types.InlineKeyboardButton(text="⬅️", callback_data=paginator.new(page=current_page, location="prev"))
        )
    elif current_page == 1:
        keyboard.add(
            types.InlineKeyboardButton(text="➡️", callback_data=paginator.new(page=current_page, location="next"))
        )
    else:
        keyboard.add(
            types.InlineKeyboardButton(text="⬅️", callback_data=paginator.new(page=current_page, location="prev")),
            types.InlineKeyboardButton(text="➡️", callback_data=paginator.new(page=current_page, location="next"))
        )
    return keyboard
