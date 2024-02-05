
from pydantic import BaseModel

class GroupsBase(BaseModel):
    name: str

    class Config:
        orm_mode = True

class GroupsCreate(GroupsBase):
    ...

class Groups(GroupsBase):
    idGroup: int
    Curator: ... # TODO: ADD Teachers
