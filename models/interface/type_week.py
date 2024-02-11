
from pydantic import BaseModel

class TypeWeekBase(BaseModel):
    Name: str

    class Config:
        from_attributes = True

class TypeWeekCreate(TypeWeekBase): ...

class TypeWeek(TypeWeekBase):
    idTypeWeek: int

