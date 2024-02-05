
from pydantic import BaseModel

class RoleBase(BaseModel):
    name: str
    level: int

    class Config:
        orm_mode = True

class RoleCreate(RoleBase):
    ...

class Role(RoleBase):
    idRole: int
