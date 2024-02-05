
from pydantic import BaseModel

class DayWeeksBase(BaseModel):
    ...

    class Config:
        orm_mode = True

class DayWeeksCreate(DayWeeksBase):
    ...

class DayWeeks(DayWeeksBase):
    ...
