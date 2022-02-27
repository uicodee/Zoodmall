import typing
from loader import users


async def new_user(user_id: int, language: str) -> typing.Union[bool]:
    await users.insert_one()