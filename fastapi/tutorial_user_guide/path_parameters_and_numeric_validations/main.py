"""Path Parameters and Numeric Validations"""
# In the same way that you can declare more validations and metadata for query parameters with Query,
# you can declare the same type of validations and metadata for path parameters with Path.
from typing import Annotated
from fastapi import FastAPI, Query, Path

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(item_id: Annotated[int, Path(title="The ID of the Item to get")], q: Annotated[str | None, Query(alias="item-query")] = None):
    """Read Items"""
    results = {"item_id": int(item_id)}
    if q:
        results.update({"q": q})
    return results
