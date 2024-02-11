
from pydantic import BaseModel

from teachers import Teachers
from class_ import Class
from classrooms import Classrooms

class TeachersClassBase(BaseModel):
    Teacher: Teachers
    Class: Class
    Classrooms: Classrooms

    class Config:
        from_attributes = True

class TeachersClassCreate(TeachersClassBase):
    ...

class TeachersClass(TeachersClassBase):
    idTeacherClasses: int
