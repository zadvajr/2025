from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from pydantic import BaseModel
from database import get_db
from models import User

app = FastAPI()

class Users(BaseModel):
    name: str,
    email: str,
    db: AsyncSession = Depends(get_db)

@app.get("/")
async def root():
    return {"message": "FastAPI + PostgreSQL"}

@app.post("/users/")
async def create_user(user: Users):
    new_user = User(name=user.name, email=user.email)
