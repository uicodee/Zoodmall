from pydantic import BaseModel
from typing import List


# Products list schema

class Data(BaseModel):
    productId: int
    name: str


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

# Detail list schema


class Installment(BaseModel):
    installmentTimeTxt: str
    installmentAmountTxt: str


class Specifics(BaseModel):
    name: str
    value: str


class DetailProduct(BaseModel):
    name: str
    price: float
    defaultPrice: float
    specifics: List[Specifics]
    description: str
    productImages: List
    # installmentsInfo: Installment = None


class Result(BaseModel):
    Product: DetailProduct


class Detail(BaseModel):
    success: bool
    status: int
    message: str
    result: Result