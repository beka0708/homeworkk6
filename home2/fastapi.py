# print('Hello')
# import fastapi
from typing import Union
from starlette.responses import JSONResponse
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

