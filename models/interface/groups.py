
from pydantic import BaseModel

from models.interface.teachers import Teachers

class GroupsBase(BaseModel):
    name: str

    class Config:
        from_attributes = True

class GroupsCreate(GroupsBase):
    ...

class Groups(GroupsBase):
    idGroup: int
    Curator: Teachers | None  # TODO: ADD Teachers
