
from pydantic import BaseModel

class TimeClassBase(BaseModel):
    ...

    class Config:
        orm_mode = True

class TimeClassCreate(TimeClassBase):
    ...

class TimeClass(TimeClassBase):
    ...
