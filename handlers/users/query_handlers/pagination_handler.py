import typing

from aiogram.dispatcher import FSMContext

from keyboards.inline import pagination
from loader import dp, _
from aiogram import types
from callback_datas import paginator
from utils.api import Zoodmall, Response
from utils.db_api import get_language


@dp.callback_query_handler(paginator.filter())
async def pagination_handler(query: types.CallbackQuery, callback_data: typing.Dict, state: FSMContext):
    zoodmall = Zoodmall(
        limit=10,
        language=(await get_language(user_id=query.from_user.id)).get('language')
    )
    request = (await state.get_data()).get('request')
    location = callback_data.get('location')
    page = int(callback_data.get('page'))
    names = ""
    d = []
    current_page = 0
    total_page, pages = None, None
    if location == "next":
        current_page = page + 1
        data: Response = Response.parse_raw(await zoodmall.get_products(request=request, page=current_page))
        print(data)
        for index, item in enumerate(data.result.products):
            names += f"{item.name}\n"
            d.append({
                str(index + 1): item.productId
            })
            total_page, pages = data.result.pagination.totalPage, data.result.pagination.page
    elif location == "prev":
        current_page = page - 1
        data: Response = Response.parse_raw(await zoodmall.get_products(request=request, page=current_page))
        for index, item in enumerate(data.result.products):
            names += f"{item.name}\n"
            d.append({
                str(index + 1): item.productId
            })
            total_page, page = data.result.pagination.totalPage, data.result.pagination.page

    await query.message.edit_text(
        text=_("<b>{} dan {} chi saxifa</b>\n\n").format(total_page, pages) + names,
        reply_markup=pagination(
            data=d,
            max_pages=total_page,
            current_page=current_page
        )
    )
