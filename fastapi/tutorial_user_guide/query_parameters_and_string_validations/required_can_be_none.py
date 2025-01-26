"""Required Can Be None"""
# You can declare that a parameter can accept None, but that it's still required.
# This would force clients to send a value, even if the value is None.
# To do that, you can declare that None is a valid type but still use ... as the default:
from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(min_length=3)] = ...):
    """Read Items EndPoint"""
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
