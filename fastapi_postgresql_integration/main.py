from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
# from pydantic import BaseModel
from database import get_db
from models import User

app = FastAPI()

# class Users(BaseModel):
#     name: str
#     email: str

@app.get("/")
async def root():
    return {"message": "FastAPI + PostgreSQL"}

@app.post("/users/")
async def create_user(name: str, email: str, db: AsyncSession = Depends(get_db)):
    new_user = User(name=name, email=email)
    db.add(new_user)
    await db.commit()
    return {"message": "User created successfully"}

@app.get("/users/")
async def get_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User))
    users = result.scalars().all()
    return users