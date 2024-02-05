
from pydantic import BaseModel

class TokenTypeBase(BaseModel):
    ...

    class Config:
        orm_mode = True

class TokenTypeCreate(TokenTypeBase):
    ...

class TokenType(TokenTypeBase):
    ...
