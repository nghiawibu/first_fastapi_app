from sqlalchemy import String, BigInteger, ForeignKey, DATETIME
from sqlalchemy.orm import mapped_column
from ..database import Base
from datetime import datetime

class ChatLines(Base):
    __tablename__ = "chatLines"

    id = mapped_column(BigInteger, primary_key=True)
    userId = mapped_column(ForeignKey("users.id"))
    chatId = mapped_column(ForeignKey("chats.id"))
    chatLine = mapped_column(String)
    lineType = mapped_column(String)
    date = mapped_column(DATETIME, default=datetime.now)