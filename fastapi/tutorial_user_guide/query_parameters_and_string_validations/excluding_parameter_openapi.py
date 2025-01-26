"""Exclude parameters from OpenAPI"""
# To exclude a query parameter from the generated OpenAPI schema
# (and thus, from the automatic documentation systems), set the parameter include_in_schema of Query to False:
from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(include_in_schema=False)] = None):
    """Read Items EndPoint"""
    if q:
        return {"q": q}
    return {"q": "No parameter found!"}