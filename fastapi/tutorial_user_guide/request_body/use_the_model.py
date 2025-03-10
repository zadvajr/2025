"""Use the Model"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    """Item Class Model"""
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.post("/items")
async def create_new_item(item: Item):
    """create new item endpoint"""
    item_dict = item.model_dump()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict
