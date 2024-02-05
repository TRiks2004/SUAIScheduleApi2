
from pydantic import BaseModel

from time_class import TimeClass
from day_weeks import DayWeeks
from type_week import TypeWeek
from subjects import Subjects

class ClassBase(BaseModel):
    timeClasses: TimeClass
    dayWeek: DayWeeks
    typeWeek: TypeWeek
    subjects: Subjects

    class Config:
        orm_mode = True

class ClassCreate(ClassBase):
    ...

class Class(ClassBase):
    idClasses: int
