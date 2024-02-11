from datetime import datetime
from pydantic import BaseModel

from role import Role
from groups import Groups

class UsersBase(BaseModel):
    name: str
    surname: str
    Patronymic: str | None
    gender: str
    role: Role
    portrait: str
    email: str
    PhoneNumber: str | None
    birthday: datetime | None
    login: str
    password: str
    idGroup: Groups

    class Config:
        from_attributes = True

class UsersCreate(UsersBase):
    ...

class Users(UsersBase):
    idUsers: int
