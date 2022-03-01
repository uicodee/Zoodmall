from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from loader import dp, i18n, _
from aiogram import types
from states import Search
__ = i18n.lazy_gettext


@dp.message_handler(Text(equals=__('🔍 Qidirish')), state="*")
async def search(message: types.Message, state: FSMContext):
    await state.reset_state(with_data=True)
    await message.answer(
        text=_("Qidirmoqchi bo'lgan maxsulotingizni kiriting")
    )
    await Search.name.set()
