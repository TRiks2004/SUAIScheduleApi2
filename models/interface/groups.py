
from pydantic import BaseModel

class GroupsBase(BaseModel):
    name: str

    class Config:
        from_attributes = True

class GroupsCreate(GroupsBase):
    ...

class Groups(GroupsBase):
    idGroup: int
    Curator: ... # TODO: ADD Teachers
