
from pydantic import BaseModel

class ClassroomsBase(BaseModel):
    Name: str
    Building: str
    vector: int

    class Config:
        from_attributes = True

class ClassroomsCreate(ClassroomsBase):
    ...

class Classrooms(ClassroomsBase):
    idClassroom: int
