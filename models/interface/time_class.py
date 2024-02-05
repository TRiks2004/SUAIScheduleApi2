
from pydantic import BaseModel

"""
class TimeClass(Base):
    __tablename__ = 'TimeClass'

    idTimeClasses = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=False)
    beginTime = Column(Time(timezone=False), nullable=False, unique=True)
    endTime = Column(Time(timezone=False), nullable=False, unique=True)
"""

class TimeClassBase(BaseModel):
    ...

    class Config:
        orm_mode = True

class TimeClassCreate(TimeClassBase):
    ...

class TimeClass(TimeClassBase):
    ...
