from sqlalchemy import (
    Table, Column, Integer, String, MetaData, ForeignKey, Time, TIMESTAMP, Boolean, UUID,
)

from uuid import uuid4

from sqlalchemy.orm import declarative_base

Base = declarative_base()

"""
    CREATE TABLE IF NOT EXISTS TimeClass(
        idTimeClasses SERIAL PRIMARY KEY NOT NULL,
        number int NOT NULL,
        beginTime time NOT NULL,
        endTime time NOT NULL
    );
"""

class TimeClass(Base):
    __tablename__ = 'TimeClass'

    idTimeClasses = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=False)
    beginTime = Column(Time(timezone=False), nullable=False, unique=True)
    endTime = Column(Time(timezone=False), nullable=False, unique=True)


"""
    CREATE TABLE IF NOT EXISTS DayWeeks(
        idDayWeek SERIAL PRIMARY KEY NOT NULL,
        Name varchar(25) NOT NULL,
        WekEnd bool NOT NULL
    );
"""

class DayWeeks(Base):
    __tablename__ = 'DayWeeks'

    idDayWeek = Column(Integer, primary_key=True)
    Name = Column(String(25), nullable=False, unique=True)
    WekEnd = Column(Boolean, nullable=False)

"""
    CREATE TABLE IF NOT EXISTS TypeWeek(
        idTypeWeek SERIAL PRIMARY KEY NOT NULL,
        Name varchar(40) NOT NULL
    );
"""

class TypeWeek(Base):
    __tablename__ = 'TypeWeek'

    idTypeWeek = Column(Integer, primary_key=True)
    Name = Column(String(40), nullable=False, unique=True)

"""
    CREATE TABLE IF NOT EXISTS Teachers(
        idTeacher SERIAL PRIMARY KEY NOT NULL,
        Surname varchar(40) NOT NULL,
        Name varchar(40) NOT NULL,
        Patronymic varchar(40) NOT NULL,
        email varchar(255) NOT NULL,
        phoneNumber varchar(10) NOT NULL
    );
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
    CREATE TABLE IF NOT EXISTS Classrooms(
        idClassroom SERIAL PRIMARY KEY NOT NULL,
        Name varchar(10) NOT NULL,
        Building varchar(45) NOT NULL,
        vector bool
    );
"""

class Classrooms(Base):
    __tablename__ = 'Classrooms'

    idClassroom = Column(Integer, primary_key=True)
    Name = Column(String(10), nullable=False)
    Building = Column(String(45), nullable=False)
    vector = Column(Integer, nullable=False)

"""
    CREATE TABLE IF NOT EXISTS Subjects(
        idSubject serial PRIMARY KEY NOT NULL,
        Name varchar(255) NOT NULL
    );
"""

class Subjects(Base):
    __tablename__ = 'Subjects'

    idSubject = Column(Integer, primary_key=True)
    Name = Column(String(255), nullable=False, unique=True)

"""
    CREATE TABLE IF NOT EXISTS Class(
        idClasses SERIAL PRIMARY KEY NOT NULL,
        timeClasses int NOT NULL REFERENCES TimeClass(idTimeClasses),
        dayWeek int NOT NULL REFERENCES DayWeeks(idDayWeek),
        typeWeek int NOT NULL REFERENCES TypeWeek(idTypeWeek),
        subjects int NOT NULL REFERENCES Subjects(idSubject)
    );
"""

class Class(Base):
    __tablename__ = 'Class'

    idClasses = Column(Integer, primary_key=True)
    
    # TODO: Уникальное сочетание Полей
    timeClasses = Column(Integer, ForeignKey(TimeClass.idTimeClasses), nullable=False)
    dayWeek = Column(Integer, ForeignKey(DayWeeks.idDayWeek), nullable=False)
    typeWeek = Column(Integer, ForeignKey(TypeWeek.idTypeWeek), nullable=False)
    subjects = Column(Integer, ForeignKey(Subjects.idSubject), nullable=False)



"""
    CREATE TABLE IF NOT EXISTS Groups(
        idGroup SERIAL PRIMARY KEY NOT NULL,
        name varchar(10) NOT NULL,
        Curator int REFERENCES Teachers(idTeacher)
    );
"""

class Groups(Base):
    __tablename__ = 'Groups'

    idGroup = Column(Integer, primary_key=True)
    name = Column(String(10), nullable=False, unique=True)
    Curator = Column(Integer, ForeignKey(Teachers.idTeacher))

"""
    CREATE TABLE IF NOT EXISTS TeachersClass(
        idTeacherClasses SERIAL PRIMARY KEY NOT NULL,
        idTeacher int NOT NULL REFERENCES Teachers(idTeacher),
        idClass int NOT NULL REFERENCES Class(idClasses),
        ---------------------------------------------
        idClassrooms int NOT NULL REFERENCES Classrooms(idClassroom),
        subgroup int4 NOT NULL
    );
"""

class TeachersClass(Base):
    __tablename__ = 'TeachersClass'

    idTeacherClasses = Column(Integer, primary_key=True)

    # TODO: Уникальное сочетание Полей
    idTeacher = Column(Integer, ForeignKey(Teachers.idTeacher), nullable=False)
    idClass = Column(Integer, ForeignKey(Class.idClasses), nullable=False)
    idClassrooms = Column(Integer, ForeignKey(Classrooms.idClassroom), nullable=False)

"""
    CREATE TABLE IF NOT EXISTS TokenType(
        idTokenType SERIAL PRIMARY KEY NOT NULL,
        name varchar(255) NOT NULL
    );
"""

class TokenType(Base):
    __tablename__ = 'TokenType'

    idTokenType = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)

"""
    CREATE TABLE IF NOT EXISTS Token(
        idToken UUID PRIMARY KEY NOT NULL,
        token varchar(255) NOT NULL,
        tokenType INT NOT NULL REFERENCES TokenType(idTokenType),
        created_at TIMESTAMP NOT NULL
    );
"""

class Token(Base):
    __tablename__ = 'Token'

    idToken = Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    token = Column(String(255), nullable=False,  unique=True)
    tokenType = Column(Integer, ForeignKey(TokenType.idTokenType), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False)

"""
    CREATE TABLE IF NOT EXISTS Role(
        idRole SERIAL PRIMARY KEY NOT NULL,
        name varchar(255) NOT NULL,
        level int NOT NULL DEFAULT 0
    );
"""

class Role(Base):
    __tablename__ = 'Role'

    idRole = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    level = Column(Integer, nullable=False, default=0)

"""
    CREATE TABLE IF NOT EXISTS Users(
        idUsers UUID PRIMARY KEY NOT NULL,
        name varchar(45) NOT NULL,
        surname varchar(45) NOT NULL,
        gender varchar(10) NOT NULL,
        role int NOT NULL REFERENCES Role(idRole),
        portrait varchar(255) NOT NULL,
        email varchar(255) NOT NULL UNIQUE,
        PhoneNumber varchar(10) NOT NULL UNIQUE,
        birthday date,
        login varchar(255) NOT NULL UNIQUE,
        password varchar(30) NOT NULL,
        idGroup int NOT NULL REFERENCES Groups(idGroup)
    );
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
    CREATE TABLE IF NOT EXISTS UserToken(
        idUserToken UUID PRIMARY KEY NOT NULL,
        idUser UUID NOT NULL REFERENCES Users(idUsers),
        idToken UUID NOT NULL REFERENCES Token(idToken)
    );
"""

class UserToken(Base):
    __tablename__ = 'UserToken'

    idUserToken = Column(UUID(as_uuid=True), primary_key=True, default=uuid4())

    # TODO: Уникальное сочетание Полей
    idUser = Column(UUID(as_uuid=True), ForeignKey(Users.idUsers), nullable=False)
    idToken = Column(UUID(as_uuid=True), ForeignKey(Token.idToken), nullable=False)

"""
    CREATE TABLE IF NOT EXISTS News(
        idNew UUID PRIMARY KEY NOT NULL,
        picture varchar(255),
        header varchar(50) NOT NULL,
        text varchar(2000) NOT NULL,
        responsible UUID NOT NULL REFERENCES Users(idUsers),
        created_at timestamp NOT NULL,
        post_date timestamp NOT NULL,
        views int NOT NULL DEFAULT 0
    );
"""

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

"""
    CREATE TABLE IF NOT EXISTS ScheduleChanges(
        idScheduleChange SERIAL PRIMARY KEY NOT NULL,
        timeClasses int NOT NULL REFERENCES TimeClass(idTimeClasses),
        subjects int NOT NULL REFERENCES Subjects(idSubject)
    );
"""

class ScheduleChanges(Base):
    __tablename__ = 'ScheduleChanges'

    idScheduleChange = Column(Integer, primary_key=True)
    timeClasses = Column(Integer, ForeignKey(TimeClass.idTimeClasses), nullable=False)
    subjects = Column(Integer, ForeignKey(Subjects.idSubject), nullable=False)

"""
    CREATE TABLE IF NOT EXISTS TeachersScheduleChanges(
        idTeacherClasses SERIAL PRIMARY KEY NOT NULL,
        idTeacher int NOT NULL REFERENCES Teachers(idTeacher),
        idClass int NOT NULL REFERENCES ScheduleChanges(idScheduleChange),
        ---------------------------------------------
        idClassrooms int NOT NULL REFERENCES Classrooms(idClassroom),
        subgroup int4 NOT NULL
    );
"""

class TeachersScheduleChanges(Base):
    __tablename__ = 'TeachersScheduleChanges'

    idTeacherClasses = Column(Integer, primary_key=True)
    idTeacher = Column(Integer, ForeignKey(Teachers.idTeacher), nullable=False)
    idClass = Column(Integer, ForeignKey(ScheduleChanges.idScheduleChange), nullable=False)
    idClassrooms = Column(Integer, ForeignKey(Classrooms.idClassroom), nullable=False)
    subgroup = Column(Integer, nullable=False)