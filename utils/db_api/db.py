from motor import motor_asyncio
from data import config


db_client = motor_asyncio.AsyncIOMotorClient(config.MONGO_HOST)
db = db_client[config.DB_NAME]
users: motor_asyncio.AsyncIOMotorCollection = db['users']
favourite: motor_asyncio.AsyncIOMotorCollection = db['favourite']


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


async def get_language(user_id: int) -> dict:

    """
    :param user_id: user's identifier
    :return: user object
    """

    data = await users.find_one({"user_id": user_id})
    return data


async def add_favourite(user_id: int, product_id: int) -> None:

    """
    :param user_id: user's identifier
    :param product_id: zoodmall product's identifier
    :return: None
    """

    await favourite.insert_one({
        "user_id": user_id,
        "product_id": product_id
    })

