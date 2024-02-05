
from pydantic import BaseModel

class TypeWeekBase(BaseModel):
    Name: str

    class Config:
        orm_mode = True

class TypeWeekCreate(TypeWeekBase): ...

class TypeWeek(TypeWeekBase):
    idTypeWeek: int

