
from pydantic import BaseModel

"""
class Groups(Base):
    __tablename__ = 'Groups'

    idGroup = Column(Integer, primary_key=True)
    name = Column(String(10), nullable=False, unique=True)
    Curator = Column(Integer, ForeignKey(Teachers.idTeacher))

"""

class GroupsBase(BaseModel):
    ...

    class Config:
        orm_mode = True

class GroupsCreate(GroupsBase):
    ...

class Groups(GroupsBase):
    ...
