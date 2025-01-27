"""Declare metadata"""
# You can declare all the same parameters as for Query.
# For example, to declare a title metadata value for the path parameter item_id you can type:
from typing import Annotated
from fastapi import FastAPI, Query, Path

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(item_id: Annotated[int, Path(title="The ID of item to get")], q: Annotated[str | None, Query(alias="query-string")] = None):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

#A path parameter is always required as it has to be part of the path.
#Even if you declared it with None or set a default value, it would not affect anything,
#it would still be always required.
