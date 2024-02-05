
from pydantic import BaseModel

class ScheduleChangesBase(BaseModel):
    ...

    class Config:
        orm_mode = True

class ScheduleChangesCreate(ScheduleChangesBase):
    ...

class ScheduleChanges(ScheduleChangesBase):
    ...
