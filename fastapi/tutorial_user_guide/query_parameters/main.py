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
async def read_items(skip: int = 0, limit: int = 10):
    return items[skip: skip + limit]

#The query is the set of key value pair that goes after the ? and separated by & symbol
#For example: http://127.0.0.1:8000/items/?skip=0&limit=10
#So the query parameters are skip: with value of 0 and limit: with value of 10
#They are naturally strings, since they are par of the URL
#But when you declare them with Python types (in the example above, as int), 
# they are converted to that type and validated against it.


#Optional Parameters
#The same way you can set optional value to query parameter by setting their default value to none
#You can set optional parameters value too:
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    #This is how you set optional parameter q: str | None = None
    """read item endpoint"""
    if q:
        print(q)
        return {"item_id": item_id, "q": q}
    print(q)
    return {"item_id": item_id}
#In this case, the function parameter q will be optional, and will be None by default.
# Also notice that FastAPI is smart enough to notice that the path parameter item_id is a path parameter 
# and q is not, so, it's a query parameter.

