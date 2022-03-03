from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from utils.db_api import is_registered


class is_user(BoundFilter):

    async def check(self, message: types.Message) -> bool:
        return await is_registered(user_id=message.from_user.id)
