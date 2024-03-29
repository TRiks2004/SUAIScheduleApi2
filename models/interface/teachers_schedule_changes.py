
from pydantic import BaseModel

from teachers import Teachers
from class_ import Class
from classrooms import Classrooms

class TeachersScheduleChangesBase(BaseModel):
    Teacher: Teachers
    Class: Class
    Classrooms: Classrooms
    subgroup: int

    class Config:
        from_attributes = True

class TeachersScheduleChangesCreate(TeachersScheduleChangesBase):
    ...

class TeachersScheduleChanges(TeachersScheduleChangesBase):
    idTeacherClasses: int
