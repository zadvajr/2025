from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from pydantic import BaseModel, EmailStr
from database import get_db
from models import User

app = FastAPI()

class Users(BaseModel):
    name: str
    email: EmailStr

@app.get("/")
async def root():
    return {"message": "FastAPI + PostgreSQL"}

@app.post("/users/")
async def create_user(user: Users, db: AsyncSession = Depends(get_db)):
    new_user = User(name=user.name, email=user.email)
    db.add(new_user)
    await db.commit()
    return {"message": "User created successfully"}

@app.get("/users/")
async def get_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User))
    users = result.scalars().all()
    return users