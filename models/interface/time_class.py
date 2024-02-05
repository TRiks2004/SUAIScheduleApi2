from pydantic import BaseModel
from datetime import time

class TimeClassBase(BaseModel):
    number: int
    beginTime: time
    endTime: time

    class Config:
        orm_mode = True

class TimeClassCreate(TimeClassBase):
    ...

class TimeClass(TimeClassBase):
    idTimeClasses: int
