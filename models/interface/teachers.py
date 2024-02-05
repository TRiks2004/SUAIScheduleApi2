
from pydantic import BaseModel

"""
class Teachers(Base):
    __tablename__ = 'Teachers'

    idTeacher = Column(Integer, primary_key=True)
    Surname = Column(String(40), nullable=False)
    Name = Column(String(40), nullable=False)
    Patronymic = Column(String(40))
    email = Column(String(255), nullable=False, unique=True)
    phoneNumber = Column(String(10), nullable=False, unique=True)
"""

class TeachersBase(BaseModel):
    ...

    class Config:
        orm_mode = True

class TeachersCreate(TeachersBase):
    ...

class Teachers(TeachersBase):
    ...
