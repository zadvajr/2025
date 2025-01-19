"""Request body"""
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class Item(BaseModel):
    """Item class model with pydantic"""
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    """create item"""
    return item
