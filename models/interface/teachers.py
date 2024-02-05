
from pydantic import BaseModel

class TeachersBase(BaseModel):
    Surname: str
    Name: str
    Patronymic: str | None
    email: str
    phoneNumber: str

    class Config:
        orm_mode = True

class TeachersCreate(TeachersBase):
    ...

class Teachers(TeachersBase):
    idTeacher: int
