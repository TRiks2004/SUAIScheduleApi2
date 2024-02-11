
from pydantic import BaseModel

class SubjectsBase(BaseModel):
    Name: str

    class Config:
        from_attributes = True

class SubjectsCreate(SubjectsBase):
    ...

class Subjects(SubjectsBase):
    idSubject: int
