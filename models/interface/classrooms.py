
from pydantic import BaseModel

"""
class Classrooms(Base):
    __tablename__ = 'Classrooms'

    idClassroom = Column(Integer, primary_key=True)
    Name = Column(String(10), nullable=False)
    Building = Column(String(45), nullable=False)
    vector = Column(Integer, nullable=False)
"""

class ClassroomsBase(BaseModel):
    ...

    class Config:
        orm_mode = True

class ClassroomsCreate(ClassroomsBase):
    ...

class Classrooms(ClassroomsBase):
    ...
