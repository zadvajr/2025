#First Steps
#The simplest FastAPI file could look as follow
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}