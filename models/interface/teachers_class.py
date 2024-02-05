
from pydantic import BaseModel

class TeachersClassBase(BaseModel):
    ...

    class Config:
        orm_mode = True

class TeachersClassCreate(TeachersClassBase):
    ...

class TeachersClass(TeachersClassBase):
    ...
