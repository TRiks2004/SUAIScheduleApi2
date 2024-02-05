from sqlalchemy import (
    Table, Column, Integer, String, MetaData, ForeignKey, Time, TIMESTAMP, Boolean, UUID, UniqueConstraint
)

from uuid import uuid4

from sqlalchemy.orm import declarative_base

Base = declarative_base()

class TimeClass(Base):
    __tablename__ = 'TimeClass'

    idTimeClasses = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=False)
    beginTime = Column(Time(timezone=False), nullable=False, unique=True)
    endTime = Column(Time(timezone=False), nullable=False, unique=True)

class DayWeeks(Base):
    __tablename__ = 'DayWeeks'

    idDayWeek = Column(Integer, primary_key=True)
    Name = Column(String(25), nullable=False, unique=True)
    WekEnd = Column(Boolean, nullable=False)

class TypeWeek(Base):
    __tablename__ = 'TypeWeek'

    idTypeWeek = Column(Integer, primary_key=True)
    Name = Column(String(40), nullable=False, unique=True)

class Teachers(Base):
    __tablename__ = 'Teachers'

    idTeacher = Column(Integer, primary_key=True)
    Surname = Column(String(40), nullable=False)
    Name = Column(String(40), nullable=False)
    Patronymic = Column(String(40))
    email = Column(String(255), nullable=False, unique=True)
    phoneNumber = Column(String(10), nullable=False, unique=True)

class Classrooms(Base):
    __tablename__ = 'Classrooms'

    idClassroom = Column(Integer, primary_key=True)
    Name = Column(String(10), nullable=False)
    Building = Column(String(45), nullable=False)
    vector = Column(Integer, nullable=False)

class Subjects(Base):
    __tablename__ = 'Subjects'

    idSubject = Column(Integer, primary_key=True)
    Name = Column(String(255), nullable=False, unique=True)

class Class(Base):
    __tablename__ = 'Class'

    idClasses = Column(Integer, primary_key=True)
    
    timeClasses = Column(Integer, ForeignKey(TimeClass.idTimeClasses), nullable=False)
    dayWeek = Column(Integer, ForeignKey(DayWeeks.idDayWeek), nullable=False)
    typeWeek = Column(Integer, ForeignKey(TypeWeek.idTypeWeek), nullable=False)
    subjects = Column(Integer, ForeignKey(Subjects.idSubject), nullable=False)

    __table_args__ = (
        UniqueConstraint(timeClasses, dayWeek, typeWeek, subjects),
    )

class Groups(Base):
    __tablename__ = 'Groups'

    idGroup = Column(Integer, primary_key=True)
    name = Column(String(10), nullable=False, unique=True)
    Curator = Column(Integer, ForeignKey(Teachers.idTeacher))

class TeachersClass(Base):
    __tablename__ = 'TeachersClass'

    idTeacherClasses = Column(Integer, primary_key=True)

    idTeacher = Column(Integer, ForeignKey(Teachers.idTeacher), nullable=False)
    idClass = Column(Integer, ForeignKey(Class.idClasses), nullable=False)
    idClassrooms = Column(Integer, ForeignKey(Classrooms.idClassroom), nullable=False)

    __table_args__ = (
        UniqueConstraint(idTeacher, idClass, idClassrooms),
    )

class TokenType(Base):
    __tablename__ = 'TokenType'

    idTokenType = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)

class Token(Base):
    __tablename__ = 'Token'

    idToken = Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    token = Column(String(255), nullable=False,  unique=True)
    tokenType = Column(Integer, ForeignKey(TokenType.idTokenType), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False)
    deadToken = Column(TIMESTAMP(timezone=True), nullable=False)

class Role(Base):
    __tablename__ = 'Role'

    idRole = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    level = Column(Integer, nullable=False, default=0)

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

class UserToken(Base):
    __tablename__ = 'UserToken'

    idUserToken = Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    idUser = Column(UUID(as_uuid=True), ForeignKey(Users.idUsers), nullable=False)
    idToken = Column(UUID(as_uuid=True), ForeignKey(Token.idToken), nullable=False)

    __table_args__ = (
        UniqueConstraint(idUser, idToken),
    )

class News(Base):
    __tablename__ = 'News'

    idNew = Column(Integer, primary_key=True, default=uuid4())
    picture = Column(String(255))
    header = Column(String(50), nullable=False)
    text = Column(String(2000), nullable=False)
    responsible = Column(UUID(as_uuid=True), ForeignKey(Users.idUsers), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False)
    post_date = Column(TIMESTAMP(timezone=True), nullable=False)
    views = Column(Integer, nullable=False, default=0)

class ScheduleChanges(Base):
    __tablename__ = 'ScheduleChanges'

    idScheduleChange = Column(Integer, primary_key=True)
    timeClasses = Column(Integer, ForeignKey(TimeClass.idTimeClasses), nullable=False)
    subjects = Column(Integer, ForeignKey(Subjects.idSubject), nullable=False)

class TeachersScheduleChanges(Base):
    __tablename__ = 'TeachersScheduleChanges'

    idTeacherClasses = Column(Integer, primary_key=True)
    idTeacher = Column(Integer, ForeignKey(Teachers.idTeacher), nullable=False)
    idClass = Column(Integer, ForeignKey(ScheduleChanges.idScheduleChange), nullable=False)
    idClassrooms = Column(Integer, ForeignKey(Classrooms.idClassroom), nullable=False)
    subgroup = Column(Integer, nullable=False)


