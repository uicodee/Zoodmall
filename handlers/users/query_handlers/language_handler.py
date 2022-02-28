from aiogram import types

from callback_datas import language
from keyboards.default import menu
from loader import dp, _
from utils.db_api import *


@dp.callback_query_handler(language.filter())
async def language_handler(query: types.CallbackQuery, callback_data: dict):
    language_code = callback_data.get('language_code')
    if await is_registered(user_id=query.from_user.id):
        await update_language(user_id=query.from_user.id, language=language_code)
    else:
        await new_user(user_id=query.from_user.id, language=language_code)
    await query.message.delete()
    await query.message.answer(
        text=_("Assalomu Alaykum, xush kelibsiz!", locale=language_code),
        reply_markup=menu(_, locale=language_code)
    )