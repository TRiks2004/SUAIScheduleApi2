
from datetime import datetime
from pydantic import BaseModel
from users import Users

class NewsBase(BaseModel):
    picture: str | None
    header: str
    text: str
    responsible: Users
    created_at: datetime
    post_date: datetime
    views: int

    class Config:
        from_attributes = True

class NewsCreate(NewsBase):
    ...

class News(NewsBase):
    idNew: int
