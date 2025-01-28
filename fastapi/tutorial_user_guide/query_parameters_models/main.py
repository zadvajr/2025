"""Query Parameter Models"""
#If you have a group of query parameters that are related,
# you can create a Pydantic model to declare them.
#This would allow you to re-use the model in multiple places and also to declare validations
#and metadata for all the parameters at once.

# Query Parameters with a Pydantic Model
# Declare the query parameters that you need in a Pydantic model,
# and then declare the parameter as Query:

from typing import Annotated, Literal
from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

app = FastAPI()

class FilterParams(BaseModel):
    """Query Param Model"""
    limit: int = Field(100, ge=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []

@app.get("/items/")
async def read_items(filter_query: Annotated[FilterParams, Query()]):
    """Read Items EndPoint"""
    return filter_query
