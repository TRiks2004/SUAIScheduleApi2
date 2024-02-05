
from pydantic import BaseModel

class SubjectsBase(BaseModel):
    Name: str

    class Config:
        orm_mode = True

class SubjectsCreate(SubjectsBase):
    ...

class Subjects(SubjectsBase):
    idSubject: int
