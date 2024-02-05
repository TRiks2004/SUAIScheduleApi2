
from pydantic import BaseModel

"""
class TeachersClass(Base):
    __tablename__ = 'TeachersClass'

    idTeacherClasses = Column(Integer, primary_key=True)

    idTeacher = Column(Integer, ForeignKey(Teachers.idTeacher), nullable=False)
    idClass = Column(Integer, ForeignKey(Class.idClasses), nullable=False)
    idClassrooms = Column(Integer, ForeignKey(Classrooms.idClassroom), nullable=False)
"""

class TeachersClassBase(BaseModel):
    ...

    class Config:
        orm_mode = True

class TeachersClassCreate(TeachersClassBase):
    ...

class TeachersClass(TeachersClassBase):
    ...
