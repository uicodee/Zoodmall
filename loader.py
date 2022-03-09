from pathlib import Path

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.i18n import I18nMiddleware

from data import config

# Prepare bot
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

I18N_DOMAIN = 'mybot'
BASE_DIR = Path(__file__).parent
LOCALES_DIR = BASE_DIR / 'locales'
i18n = I18nMiddleware(I18N_DOMAIN, LOCALES_DIR)
dp.middleware.setup(i18n)
_ = i18n.gettext