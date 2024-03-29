
from pydantic import BaseModel

from time_class import TimeClass
from subjects import Subjects

class ScheduleChangesBase(BaseModel):
    timeClasses: TimeClass
    subjects: Subjects

    class Config:
        from_attributes = True

class ScheduleChangesCreate(ScheduleChangesBase):
    ...

class ScheduleChanges(ScheduleChangesBase):
    idScheduleChange: int
