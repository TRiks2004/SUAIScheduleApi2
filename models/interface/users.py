from pydantic import BaseModel

"""
class Users(Base):
    __tablename__ = 'Users'

    idUsers = Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    name = Column(String(45), nullable=False)
    surname = Column(String(45), nullable=False)
    Patronymic = Column(String(40))
    gender = Column(String(1), nullable=False)
    role = Column(Integer, ForeignKey(Role.idRole), nullable=False)
    portrait = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    PhoneNumber = Column(String(10), unique=True)
    birthday = Column(TIMESTAMP)
    login = Column(String(255), nullable=False, unique=True)
    password = Column(String(30), nullable=False)
    idGroup = Column(Integer, ForeignKey(Groups.idGroup), nullable=False)
"""

class UsersBase(BaseModel):
    ...

    class Config:
        orm_mode = True

class UsersCreate(UsersBase):
    ...

class Users(UsersBase):
    ...
