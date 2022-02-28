from aiogram import types
from aiogram.contrib.middlewares.i18n import I18nMiddleware

from utils.db_api import get_language


class ACLMiddleware(I18nMiddleware):

    async def get_user_locale(self, action, args):
        user = types.User.get_current()
        data = await get_language(user_id=user.id)
        if data:
            return data['language']
        else:
            return user.locale