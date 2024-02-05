
from pydantic import BaseModel

"""
class Subjects(Base):
    __tablename__ = 'Subjects'

    idSubject = Column(Integer, primary_key=True)
    Name = Column(String(255), nullable=False, unique=True)
"""

class SubjectsBase(BaseModel):
    ...

    class Config:
        orm_mode = True

class SubjectsCreate(SubjectsBase):
    ...

class Subjects(SubjectsBase):
    ...
