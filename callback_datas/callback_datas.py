from aiogram.utils.callback_data import CallbackData

language = CallbackData("language", "language_code")
paginator = CallbackData("paginator", "page", "location")
select = CallbackData("select", "product_id")