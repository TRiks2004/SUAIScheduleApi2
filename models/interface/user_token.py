
from pydantic import BaseModel

class UserTokenBase(BaseModel):
    ...

    class Config:
        orm_mode = True

class UserTokenCreate(UserTokenBase):
    ...

class UserToken(UserTokenBase):
    ...
