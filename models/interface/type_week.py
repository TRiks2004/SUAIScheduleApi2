
from pydantic import BaseModel

class TypeWeekBase(BaseModel):
    ...

    class Config:
        orm_mode = True

class TypeWeekCreate(TypeWeekBase):
    ...

class TypeWeek(TypeWeekBase):
    ...
