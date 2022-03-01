from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, _
from states import Search
from utils.api import Zoodmall, Response
from utils.db_api import get_language
from keyboards.inline import pagination


@dp.message_handler(state=Search.name)
async def get_name(message: types.Message, state: FSMContext):
    msg = await message.answer(text="⏳")
    language = (await get_language(user_id=message.from_user.id)).get('language')
    request = message.text
    zoodmall = Zoodmall(limit=10, language=language)
    data: Response = Response.parse_raw(await zoodmall.get_products(request=request, page=1))
    names = ""
    d = []
    for index, item in enumerate(data.result.products):
        names += f"{item.name}\n"
        d.append({
            str(index + 1): item.productId
        })

    await dp.bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=msg.message_id,
        text=_("<b>{} dan {} chi saxifa</b>\n\n").format(data.result.pagination.totalPage, data.result.pagination.page) + names,
        reply_markup=pagination(
            data=d,
            max_pages=data.result.pagination.totalPage,
            current_page=data.result.pagination.page
        )
    )
