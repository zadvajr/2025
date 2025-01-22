"""Query Parameters and String Validations"""
#FastAPI allows you to declare additional information and validations for your parameters
#For example
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/")
async def read_items(q: str | None = None):
    """Read Items Endpoint"""
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
