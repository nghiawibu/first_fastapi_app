from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column
from ..database import Base

class User(Base):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True)
    userName = mapped_column(String)
    # hashedPassword = mapped_column(String)

class Chat(Base):
    __tablename__ = "chats"
    
    id = mapped_column(Integer, primary_key=True)