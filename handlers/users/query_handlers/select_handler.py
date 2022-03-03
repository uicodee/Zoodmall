from loader import dp, _
from aiogram import types
from callback_datas import select
from utils.api import Zoodmall
from utils.db_api import get_language
from utils.api import schemas
from aiogram import md


@dp.callback_query_handler(select.filter())
async def select_handler(query: types.CallbackQuery, callback_data: dict) -> None:
    language = (await get_language(user_id=query.from_user.id)).get('language')
    product_id = int(callback_data.get('product_id'))
    zoodmall = Zoodmall(language=language)
    data = await zoodmall.get_details(product_id=product_id)
    # print(data)
    result = schemas.Detail.parse_raw(data)
    print(result)
    info = _(
        "📃 Nomi: {name}\n"
        "💰 Xozirgi narxi: {price}\n"
        "💸 Odatdagi narxi: {default_price}\n"
        "📊 Xususiyatlari: \n{specifics}"
        "🗒 Ta'rif: {description}\n"
    )
    specific = [f"<b>{x.name}</b>: {x.value}\n" for x in result.result.Product.specifics]
    # print(specific)
    await query.message.edit_text(
        text=info.format(
            name=md.hlink(
                title=result.result.Product.name,
                url=result.result.Product.productImages[-2]
            ),
            price=result.result.Product.price,
            default_price=result.result.Product.defaultPrice,
            specifics="".join(specific),
            description=result.result.Product.description.replace("<br />", "\n")
        )
    )