#Query Parameters
#When you declare other function parameters that are not part of path parameters, 
#they are automatically interpreted as query parameters.
from fastapi import FastAPI

app = FastAPI()

items = [
    {
        "id": 1,
        "item_name": "Car",
        "price": 2400
    },
    {
        "id": 2,
        "item_name": "Motorcycle",
        "price": 1200
    },
    {
        "id": 3,
        "item_name": "Bicycle",
        "price": 800
    }
]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return items[skip: skip + limit]