
from pydantic import BaseModel

"""
class ScheduleChanges(Base):
    __tablename__ = 'ScheduleChanges'

    idScheduleChange = Column(Integer, primary_key=True)
    timeClasses = Column(Integer, ForeignKey(TimeClass.idTimeClasses), nullable=False)
    subjects = Column(Integer, ForeignKey(Subjects.idSubject), nullable=False)
"""

class ScheduleChangesBase(BaseModel):
    ...

    class Config:
        orm_mode = True

class ScheduleChangesCreate(ScheduleChangesBase):
    ...

class ScheduleChanges(ScheduleChangesBase):
    ...
