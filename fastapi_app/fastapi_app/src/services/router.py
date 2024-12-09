from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from . import service, models, schemas
from src.database import SessionLocal, engine, get_db
from src.main import app

models.Base.metadata.create_all(bind=engine)



@app.post("/chat_lines/", response_model=schemas.ChatLine)
def create_chat_line(chat_line: schemas.ChatLineCreate, db: Session = Depends(get_db)):
    return service.create_chat_line(db=db, chat_line=chat_line)

@app.get("/chat_lines/{chat_line_id}", response_model=schemas.ChatLine)
def read_chat_line(chat_line_id: int, db: Session = Depends(get_db)):
    db_chat_line = service.get_chat_line(db, chat_line_id=chat_line_id)
    if db_chat_line is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_chat_line

@app.get("/chat_lines/", response_model=list[schemas.ChatLine])
def read_chat_lines(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    chat_lines = service.get_chat_lines(db, skip=skip, limit=limit)
    return chat_lines