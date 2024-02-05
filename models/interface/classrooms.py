
from pydantic import BaseModel

class ClassroomsBase(BaseModel):
    ...

    class Config:
        orm_mode = True

class ClassroomsCreate(ClassroomsBase):
    ...

class Classrooms(ClassroomsBase):
    ...
