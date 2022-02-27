import aiohttp
from data.config import host
from .zoodmall_exception import ZoodmallException


class Zoodmall:

    def __init__(self, limit: int, language: str):
        self.data = {
            'x-lang': language.lower(),
            'x-marketcode': 'UZ'
        }
        self.session = aiohttp.ClientSession(headers=self.data)
        self.host = host + f"?deviceType=web&nocache=true&limit={limit}"

    @staticmethod
    async def _check_response(response: aiohttp.ClientResponse):
        data: dict = await response.json(encoding="utf-8")
        if data.get('success') is True and data.get('status') == 200:
            return True
        else:
            return False

    async def get_products(self, request: str, page: int):
        async with self.session.get(url=self.host + f"&categoryId=0&nameLike={request}&page={page}&sort=1") as response:
            if await self._check_response(response=response) is False:
                raise ZoodmallException('Response is not valid')
            else:
                data: str = await response.text(encoding="utf-8")
                return data

