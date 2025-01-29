"""Body - Multiple Parameters"""
# Now that we have seen how to use Path and Query,
# let's see more advanced uses of request body declarations.

# Mix Path, Query and body parameters
# First, of course, you can mix Path, Query and request body parameter declarations freely
# and FastAPI will know what to do.
# And you can also declare body parameters as optional, by setting the default to None:
from typing import Annotated
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    """Item Model"""
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.put("/items/{item_id}")
async def update_item(
    item_id: Annotated[int, Path(title="The ID of the Item to get", ge=0, le=1000)],
    q: str | None = None,
    item: Item | None = None
    ):
    """Read Items Endpoint"""
    results = {"item_id": item_id}

    if q:
        results.update({"q": quit})
    if item:
        results.update({"item": item})
    return results

