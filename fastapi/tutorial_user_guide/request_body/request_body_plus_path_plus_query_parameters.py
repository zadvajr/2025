"""Request body + path + query parameters"""
#You can also declare body, path and query parameters all at the same time.
#FastAPI will recognize each of them and take data from the correct place
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    results = {"item_id": item_id, **item.model_dump()}
    if q:
        results.update({"q": q})
    return results
