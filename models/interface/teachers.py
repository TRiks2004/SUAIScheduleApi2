
from pydantic import BaseModel

class TeachersBase(BaseModel):
    ...

    class Config:
        orm_mode = True

class TeachersCreate(TeachersBase):
    ...

class Teachers(TeachersBase):
    ...
