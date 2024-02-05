
from pydantic import BaseModel

# idClasses
# timeClasses
# dayWeek
# typeWeek
# subjects

class ClassBase(BaseModel):
    ...

    class Config:
        orm_mode = True

class ClassCreate(ClassBase):
    ...

class Class(ClassBase):
    ...
