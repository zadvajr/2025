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

#Query Parameter: Type conversion
#You can declare bool type and they will be converted
@app.get("/books/{book_id}")
async def read_book(book_id: str, q: str | None = None, short: bool = False):
    """read a book"""
    book = {"book_id": book_id}
    if q:
        book.update({"q": q})
    if not short:
        book.update({
            "description": "This is a good book with a long description"
        })
    return book

#in this case if you go to:
#http://127.0.0.1:8000/items/foo?short=1 or
#http://127.0.0.1:8000/items/foo?short=True or 
#http://127.0.0.1:8000/items/foo?short=true or 
#http://127.0.0.1:8000/items/foo?short=on or
# # http://127.0.0.1:8000/items/foo?short=yes
# or any other case variation (uppercase, first letter in uppercase, etc),
# your function will see the parameter short with a bool value of True. Otherwise as False.

#Multiple path and query parameters.
#You can declare multiple path and query parameters at the same time
#FastAPI will know which one is path or query parameter.
#You don't have to declare them in a specific order or anything.
#FastAPI will detect it by name.
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: str, q: str | None = None, short: bool = False):
    """Endpoint with multiple path and query parameters"""
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "This is an amazing item that has a long description"})
    return item

#Required query parameters
# When you declare a default value for non-path parameters (for now, we have only seen query parameters),
# then it is not required.
# If you don't want to add a specific value but just make it optional, set the default as None.
# But when you want to make a query parameter required, you can just not declare any default value:
@app.get("/items/{id}")
async def read_user_and_item(id: str, needy: str):
    return {"item_id": id, "needy": needy}

# Here the query parameter needy is a required query parameter of type str.
# If you open in your browser a URL like:
# http://127.0.0.1:8000/items/foo-item
# ...without adding the required parameter needy, you will see an error like:
"""
{
  "detail": [
    {
      "type": "missing",
      "loc": [
        "query",
        "needy"
      ],
      "msg": "Field required",
      "input": null,
      "url": "https://errors.pydantic.dev/2.1/v/missing"
    }
  ]
}
"""
# As needy is a required parameter, you would need to set it in the URL:
# http://127.0.0.1:8000/items/foo-item?needy=sooooneedy
# ...this would work:
"""{
    "item_id": "foo-item",
    "needy": "sooooneedy"
}"""
# And of course, you can define some parameters as required, some as having a default value, 
# and some entirely optional: