from pydantic import BaseModel

class UsersBase(BaseModel):
    ...

    class Config:
        orm_mode = True

class UsersCreate(UsersBase):
    ...

class Users(UsersBase):
    ...
