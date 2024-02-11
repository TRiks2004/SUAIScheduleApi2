from pydantic import BaseModel
from datetime import time

class TimeClassBase(BaseModel):
    number: int
    beginTime: time
    endTime: time

    class Config:
        from_attributes = True

class TimeClassCreate(TimeClassBase):
    ...

class TimeClass(TimeClassBase):
    idTimeClasses: int
