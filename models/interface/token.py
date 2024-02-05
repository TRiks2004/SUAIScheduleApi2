
from pydantic import BaseModel

class TokenBase(BaseModel):
    ...

    class Config:
        orm_mode = True

class TokenCreate(TokenBase):
    ...

class Token(TokenBase):
    ...
