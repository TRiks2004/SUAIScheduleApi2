
from pydantic import BaseModel
from uuid import UUID
from datetime import timedelta

import token_type

from datetime import datetime

class TokenBase(BaseModel):
    token: str
    tokenType: token_type.TokenTypeBase
    created_at: datetime
    deadToken: datetime

    class Config:
        orm_mode = True

class TokenCreate(TokenBase):
    ...

class Token(TokenBase):
    idToken: UUID
