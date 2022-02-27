from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware
from utils.db_api import get_language


class Language(BaseMiddleware):

    async def on_process_message(self, message: types.Message, data: dict):
        language = await get_language(user_id=message.from_user.id)
        data["language"] = language

    async def on_process_callback_query(self, callback_query: types.CallbackQuery, data: dict):
        language = await get_language(user_id=callback_query.from_user.id)
        data["language"] = language