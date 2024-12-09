from sqlalchemy.orm import Session
from . import models, schemas

def get_chat_line(db: Session, chat_line_id: int):
    return db.query(models.ChatLines).filter(models.ChatLines.id == chat_line_id).first()

def get_chat_lines(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.ChatLines).offset(skip).limit(limit).all()

def create_chat_line(db: Session, chat_line: schemas.ChatLineCreate):
    db_chat_line = models.ChatLines(chatLine=chat_line.chatLine)
    db.add(db_chat_line)
    db.commit()
    db.refresh(db_chat_line)
    return db_chat_line