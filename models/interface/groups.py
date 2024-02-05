
from pydantic import BaseModel

class GroupsBase(BaseModel):
    ...

    class Config:
        orm_mode = True

class GroupsCreate(GroupsBase):
    ...

class Groups(GroupsBase):
    ...
