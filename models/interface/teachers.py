
from pydantic import BaseModel

class TeachersBase(BaseModel):
    Surname: str
    Name: str
    Patronymic: str | None
    email: str
    phoneNumber: str

    class Config:
        from_attributes = True

class TeachersCreate(TeachersBase):
    ...

class Teachers(TeachersBase):
    idTeacher: int
