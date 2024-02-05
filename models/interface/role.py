
from pydantic import BaseModel

class RoleBase(BaseModel):
    ...

    class Config:
        orm_mode = True

class RoleCreate(RoleBase):
    ...

class Role(RoleBase):
    ...
