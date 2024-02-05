
from pydantic import BaseModel

class TeachersScheduleChangesBase(BaseModel):
    ...

    class Config:
        orm_mode = True

class TeachersScheduleChangesCreate(TeachersScheduleChangesBase):
    ...

class TeachersScheduleChanges(TeachersScheduleChangesBase):
    ...
