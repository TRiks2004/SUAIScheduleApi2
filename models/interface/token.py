
from pydantic import BaseModel

"""
class Token(Base):
    __tablename__ = 'Token'

    idToken = Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    token = Column(String(255), nullable=False,  unique=True)
    tokenType = Column(Integer, ForeignKey(TokenType.idTokenType), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False)
    deadToken = Column(TIMESTAMP(timezone=True), nullable=False)
"""

class TokenBase(BaseModel):
    ...

    class Config:
        orm_mode = True

class TokenCreate(TokenBase):
    ...

class Token(TokenBase):
    ...
