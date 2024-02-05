
from pydantic import BaseModel

"""
class Role(Base):
    __tablename__ = 'Role'

    idRole = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    level = Column(Integer, nullable=False, default=0)
"""

class RoleBase(BaseModel):
    ...

    class Config:
        orm_mode = True

class RoleCreate(RoleBase):
    ...

class Role(RoleBase):
    ...
