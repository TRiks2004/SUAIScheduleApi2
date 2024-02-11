
from pydantic import BaseModel

from uuid import UUID

from users import Users
from token import Token

class UserTokenBase(BaseModel):
    User: Users
    Token: Token

    class Config:
        from_attributes = True

class UserTokenCreate(UserTokenBase):
    ...

class UserToken(UserTokenBase):
    idUserToken: UUID
