from typing import Annotated
from .schemas import User
from .service import get_current_user
from fastapi import Depends, FastAPI
from src.main import app

@app.get("/users/me")
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user


