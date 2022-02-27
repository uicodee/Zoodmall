from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from motor import motor_asyncio
from data import config

# Prepare bot
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Prepare DB
db_client: motor_asyncio.AsyncIOMotorClient = motor_asyncio.AsyncIOMotorClient(config.MONGO_HOST)
db = db_client[config.DB_NAME]
users = db["users"]
