from motor import motor_asyncio
from data import config


db_client = motor_asyncio.AsyncIOMotorClient(config.MONGO_HOST)
db = db_client[config.DB_NAME]
users: motor_asyncio.AsyncIOMotorCollection = db['users']


async def new_user(user_id: int, language: str) -> None:

    """
    :param user_id: user's identifier
    :param language: user's language
    :return: None
    """

    await users.insert_one({
        "user_id": user_id,
        "language": language
    })


async def is_registered(user_id: int) -> bool:

    """
    :param user_id: user's identifier
    :return: True if user is registered else False
    """

    if await users.count_documents({"user_id": user_id}) == 0:
        return False
    else:
        return True


async def update_language(user_id: int, language: str) -> None:

    """
    :param user_id: user's identifier
    :param language: user's language
    :return: None
    """

    await users.update_one(
        {"user_id": user_id},
        {"$set": {"language": language}}
    )


async def get_language(user_id: int) -> str:

    """
    :param user_id: user's identifier
    :return: user's selected language
    """

    language = (await users.find_one({"user_id": user_id})).get("language")
    return language