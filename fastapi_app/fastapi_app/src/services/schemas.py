from pydantic import BaseModel

class ChatLineBase(BaseModel):
    userId: int
    chatId: int
    chatLine: str
    lineType: str

class ChatLineCreate(ChatLineBase):
    pass

class ChatLine(ChatLineBase):
    id: int
    
    class Config:
        orm_mode: True