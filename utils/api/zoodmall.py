import aiohttp
from data.config import host
from .zoodmall_exception import ZoodmallException


class Zoodmall:

    def __init__(self, language: str):
        self.data = {
            'x-lang': language.lower(),
            'x-marketcode': 'UZ'
        }
        self.session = aiohttp.ClientSession(headers=self.data)

    async def close_session(self):
        await self.session.close()

    @staticmethod
    async def _check_response(response: aiohttp.ClientResponse):
        data: dict = await response.json(encoding="utf-8")
        if data.get('success') is True and data.get('status') == 200:
            return True
        else:
            return False

    async def get_products(self, request: str, page: int, limit: int):
        async with self.session.get(
                url=host + f"/list?deviceType=web&nocache=true&limit={limit}&categoryId=0&nameLike={request}&page={page}&sort=1"
        ) as response:
            if await self._check_response(response=response) is False:
                raise ZoodmallException('Response is not valid')
            else:
                data: str = await response.text(encoding="utf-8")
                await self.close_session()
                return data

    async def get_details(self, product_id: int):
        async with self.session.get(url=host + f"/detail?productId={product_id}") as response:
            if await self._check_response(response=response) is False:
                raise ZoodmallException('Response is not valid')
            else:
                data: str = await response.text(encoding="utf-8")
                await self.close_session()
                return data
