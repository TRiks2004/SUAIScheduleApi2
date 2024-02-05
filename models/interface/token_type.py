
from pydantic import BaseModel

"""
class TokenType(Base):
    __tablename__ = 'TokenType'

    idTokenType = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
"""

class TokenTypeBase(BaseModel):
    ...

    class Config:
        orm_mode = True

class TokenTypeCreate(TokenTypeBase):
    ...

class TokenType(TokenTypeBase):
    ...
