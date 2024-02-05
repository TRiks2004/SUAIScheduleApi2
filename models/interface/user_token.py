
from pydantic import BaseModel

"""
class UserToken(Base):
    __tablename__ = 'UserToken'

    idUserToken = Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    idUser = Column(UUID(as_uuid=True), ForeignKey(Users.idUsers), nullable=False)
    idToken = Column(UUID(as_uuid=True), ForeignKey(Token.idToken), nullable=False)
"""

class UserTokenBase(BaseModel):
    ...

    class Config:
        orm_mode = True

class UserTokenCreate(UserTokenBase):
    ...

class UserToken(UserTokenBase):
    ...
