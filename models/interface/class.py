
from pydantic import BaseModel

class ClassBase(BaseModel):
    ...

    class Config:
        orm_mode = True

class ClassCreate(ClassBase):
    ...

class Class(ClassBase):
    ...
