
from pydantic import BaseModel

class RoleBase(BaseModel):
    name: str
    level: int

    class Config:
        from_attributes = True

class RoleCreate(RoleBase):
    ...

class Role(RoleBase):
    idRole: int
