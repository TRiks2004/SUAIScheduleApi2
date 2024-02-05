
from pydantic import BaseModel

class SubjectsBase(BaseModel):
    ...

    class Config:
        orm_mode = True

class SubjectsCreate(SubjectsBase):
    ...

class Subjects(SubjectsBase):
    ...
