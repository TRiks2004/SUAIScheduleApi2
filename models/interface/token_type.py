
from pydantic import BaseModel

class TokenTypeBase(BaseModel):
    name: str

    class Config:
        from_attributes = True

class TokenTypeCreate(TokenTypeBase):
    ...

class TokenType(TokenTypeBase):
    idTokenType: int
