from pydantic import BaseModel
from typing import List


class Installment(BaseModel):
    rate: int
    amount: int
    installmentCountText: str


class Data(BaseModel):
    categoryName: str
    productId: int
    name: str
    localPrice: int
    imgUrl: str
    localCrossedPrice: int
    brand: str
    installment: Installment
    totalSold: int
    totalLocalPrice: int


class Pagination(BaseModel):
    page: int
    limit: int
    totalCount: int
    totalPage: int


class Products(BaseModel):
    products: List[Data]
    pagination: Pagination


class Response(BaseModel):
    success: bool
    status: int
    message: str
    result: Products
