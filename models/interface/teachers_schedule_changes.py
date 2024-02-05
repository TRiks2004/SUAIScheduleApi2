
from pydantic import BaseModel

"""
class TeachersScheduleChanges(Base):
    __tablename__ = 'TeachersScheduleChanges'

    idTeacherClasses = Column(Integer, primary_key=True)
    idTeacher = Column(Integer, ForeignKey(Teachers.idTeacher), nullable=False)
    idClass = Column(Integer, ForeignKey(ScheduleChanges.idScheduleChange), nullable=False)
    idClassrooms = Column(Integer, ForeignKey(Classrooms.idClassroom), nullable=False)
    subgroup = Column(Integer, nullable=False)
"""

class TeachersScheduleChangesBase(BaseModel):
    ...

    class Config:
        orm_mode = True

class TeachersScheduleChangesCreate(TeachersScheduleChangesBase):
    ...

class TeachersScheduleChanges(TeachersScheduleChangesBase):
    ...
