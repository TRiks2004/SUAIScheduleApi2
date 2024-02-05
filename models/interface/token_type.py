
from pydantic import BaseModel

class TokenTypeBase(BaseModel):
    name: str

    class Config:
        orm_mode = True

class TokenTypeCreate(TokenTypeBase):
    ...

class TokenType(TokenTypeBase):
    idTokenType: int
