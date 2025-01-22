"""Additional validations"""
# We are going to enforce that even though q is optional,
# whenever it is provided, its length doesn't exceed 50 characters.

# Import Query and Annotated¶
# To achieve that, first import: Query from fastapi
# Annotated from typing (or from typing_extensions in Python below 3.9)
from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()

@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    """Read Items Endpoint with max len of 50"""
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# But now, having Query(max_length=50) inside of Annotated, 
# we are telling FastAPI that we want it to have additional validation for this value, 
# we want it to have maximum 50 characters.

# Here we are using Query() because this is a query parameter.
# Later we will see others like Path(), Body(), Header(), and Cookie(),
# that also accept the same arguments as Query().