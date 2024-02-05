
from pydantic import BaseModel

class NewsBase(BaseModel):
    ...

    class Config:
        orm_mode = True

class NewsCreate(NewsBase):
    ...

class News(NewsBase):
    ...
