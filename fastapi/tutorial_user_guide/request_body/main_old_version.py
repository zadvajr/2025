"""In older versions of python especially from python 3.8 downword"""
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    """Pydantic model for class"""
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

@app.post('/items/')
async def create_item(item: Item):
    """create item endpoint"""
    return item
