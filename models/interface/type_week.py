
from pydantic import BaseModel

"""
class TypeWeek(Base):
    __tablename__ = 'TypeWeek'

    idTypeWeek = Column(Integer, primary_key=True)
    Name = Column(String(40), nullable=False, unique=True)
"""

class TypeWeekBase(BaseModel):
    ...

    class Config:
        orm_mode = True

class TypeWeekCreate(TypeWeekBase):
    ...

class TypeWeek(TypeWeekBase):
    ...
