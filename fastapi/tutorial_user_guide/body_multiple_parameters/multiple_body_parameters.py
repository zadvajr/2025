# Multiple Body Parameters
# In the previous example, the path operation will expect a JSON body with attributes of an Item
# like:
"""
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2
}
"""

# But you can also declare multiple body parameters e.g. item and user
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    """Item Model"""
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class User(BaseModel):
    """User Model"""
    username: str
    full_name: str | None

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, user: User):
    """Path Operation to Update Item"""
    results = {"item_id": item_id, "item": item, "user": user}
    return results
