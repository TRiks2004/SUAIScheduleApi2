from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, async_session, AsyncSession
from sqlalchemy import text, insert
from common import settings_database
from models.schemes import Base

from datetime import time

from models.schemes import (
    TimeClass, DayWeeks, TypeWeek, TokenType, Role, Class, Teachers, Classrooms, Groups, Subjects, TeachersClass
)

from loguru import logger 

import json

engine_async = create_async_engine(
    url=settings_database.db_url_async,
    echo=settings_database.db_debug,
)

async_session_maker = async_sessionmaker(engine_async, expire_on_commit=False)


async def get_async_session() -> AsyncSession:
    async with async_session_maker() as session:
        yield session


def async_db_transaction(engine_async = engine_async):
    """
    Decorator to manage database connection and transaction for an asynchronous function.
    """
    def decorator(func):
        async def wrapper(*args, **kwargs):
            async with engine_async.begin() as conn:
                # Pass the connection object to the decorated function
                await func(conn, *args, **kwargs)
        return wrapper
    return decorator

# Define an asynchronous function to test the database
@async_db_transaction()
async def test_db(conn) -> None:
    rez = await conn.execute(text("SELECT 1"))
    print('tr = ', rez.fetchall())  # Print the result of the query

# Define an asynchronous function to create the database
@async_db_transaction()
async def create_db(conn):
    logger.info('create_db')
    await conn.run_sync(Base.metadata.create_all)

@async_db_transaction()
async def drop_db(conn):
    logger.info('drop_db')
    await conn.run_sync(Base.metadata.drop_all)


class DefaultInsert:
    async def insert_date(data):
        async with async_session_maker() as session:
            session.add_all(data)
            await session.commit()
            logger.info(f'insert_date: {type(data[0])}')

    async def timeclass():
        date = [
            TimeClass(number=1, beginTime=time(9, 20, 0), endTime=time(10, 55, 0)),
            TimeClass(number=2, beginTime=time(11, 5, 0), endTime=time(12, 40, 0)),
            TimeClass(number=3, beginTime=time(13, 20, 0), endTime=time(14, 55, 0)),
            TimeClass(number=4, beginTime=time(15, 5, 0), endTime=time(16, 40, 0))
        ]

        await DefaultInsert.insert_date(data=date)

    async def dayweeks():
        date = [
            DayWeeks(Name='Понедельник', WeekEnd=False),
            DayWeeks(Name='Вторник', WeekEnd=False),
            DayWeeks(Name='Среда', WeekEnd=False),
            DayWeeks(Name='Четверг', WeekEnd=False),
            DayWeeks(Name='Пятница', WeekEnd=False),
            DayWeeks(Name='Суббота', WeekEnd=False),
            DayWeeks(Name='Воскресенье', WeekEnd=True)
        ]
        
        await DefaultInsert.insert_date(data=date)
    
    async def typeweek():
        
        date = [
            TypeWeek(Name='Числитель'),
            TypeWeek(Name='Знаменатель')
        ]
        
        await DefaultInsert.insert_date(data=date)

    async def tokentype():
        date = [
            TokenType(name='Яндекс'),
            TokenType(name='Госуслуги'),
            TokenType(name='Вконтакте'),
            TokenType(name='Телеграм'),
            TokenType(name='Google'),
            TokenType(name='Одноклассники'),
            TokenType(name='Фейсбук'),
            TokenType(name='Инстаграм'),
            TokenType(name='Твиттер')
        ]

        await DefaultInsert.insert_date(data=date)

    async def role():

        date = [
            Role(name='Администратор', level=5),
            Role(name='Редактор', level=2),
            Role(name='Студент', level=0),
            Role(name='SuperUser', level=10)
        ]

        await DefaultInsert.insert_date(data=date)

class InsertShedule:

    def __init__(self, path):
        self.path = path

        
    async def insert_shedule(self):
        self.data = await self.get_data()

        self.group = await InsertShedule.get_group(self.data)

        self.class_ = await InsertShedule.get_class(self.data)

        self.classroom = await InsertShedule.get_classroom(self.data)

        self.disciplines = await InsertShedule.get_disciplines(self.data)

        self.schedule = await InsertShedule.get_schedule(self.data, self.group, self.class_, self.classroom, self.disciplines)

        await InsertShedule.insert_date(data=self.schedule['teachers_obj'].values())
        await InsertShedule.insert_date(data=self.schedule['classrooms_obj'].values())
        await InsertShedule.insert_date(data=self.schedule['groups_obj'].values())
        await InsertShedule.insert_date(data=self.schedule['subjects_obj'].values())

        await InsertShedule.insert_date(data=self.schedule['class_obj'])
        await InsertShedule.insert_date(data=self.schedule['TeachersClass_obj'])

    async def get_schedule(data, group, class_, classroom, disciplines):
        
        count_teachers = 0
        count_class = 0
        count_TeachersClass = 0
        
        teachers_obj = {}
        classrooms_obj = {}
        groups_obj = {}
        subjects_obj = {}
        class_obj = []
        TeachersClass_obj = []

        date_TimeClass = {
            1 : TimeClass(idTimeClasses=1, number=1, beginTime=time(9, 20, 0), endTime=time(10, 55, 0)),
            2 : TimeClass(idTimeClasses=2, number=2, beginTime=time(11, 5, 0), endTime=time(12, 40, 0)),
            3 : TimeClass(idTimeClasses=3, number=3, beginTime=time(13, 20, 0), endTime=time(14, 55, 0)),
            4 : TimeClass(idTimeClasses=4, number=4, beginTime=time(15, 5, 0), endTime=time(16, 40, 0))
        }

        date_DayWeeks = {
            'Понедельник' : DayWeeks(idDayWeek=1, Name='Понедельник', WeekEnd=False),
            'Вторник'     : DayWeeks(idDayWeek=2, Name='Вторник', WeekEnd=False),
            'Среда'       : DayWeeks(idDayWeek=3, Name='Среда', WeekEnd=False),
            'Четверг'     : DayWeeks(idDayWeek=4, Name='Четверг', WeekEnd=False),
            'Пятница'     : DayWeeks(idDayWeek=5, Name='Пятница', WeekEnd=False),
            'Суббота'     : DayWeeks(idDayWeek=6, Name='Суббота', WeekEnd=False),
            'Воскресенье' : DayWeeks(idDayWeek=7, Name='Воскресенье', WeekEnd=True)
        }

        date_TypeWeek = {
            1 : TypeWeek(idTypeWeek=1, Name='Числитель'),
            2 : TypeWeek(idTypeWeek=2, Name='Знаменатель')
        }

        for i, j in classroom.items():
            if classrooms_obj.get(i, None) is None:
                classrooms_obj[i] = Classrooms(
                    idClassroom = j,
                    Name = i
                )

        for i, j in group.items():
            if groups_obj.get(i, None) is None:
                groups_obj[i] = Groups(
                    idGroup = j,
                    name = i,
                    Curator = None
                )

        for i, j in class_.items():
            if i is None: continue
            if subjects_obj.get(i, None) is None:
                
                subjects_obj[i] = Subjects(
                    idSubject = j,
                    Name = i
                )
                  
        async def gen_class(schedule, index_week, had):
            nonlocal count_teachers, count_class, count_TeachersClass

            for day in schedule.values():
                for class_ in day.values():
                    if class_['name'] is None: continue
                    for t in class_['teachers']:
                        key_teachers = f"{t['name']} {t['surname']} {t['patronymic']}"
                        if teachers_obj.get(key_teachers, None) == None:
                            teachers_obj[key_teachers] = Teachers(
                                idTeacher = count_teachers,
                                Surname = t['surname'],
                                Name = t['name'],
                                Patronymic = t['patronymic'],
                                email = None,
                                phoneNumber = None,
                                portrait = t['url_image']
                            )
                            count_teachers += 1

            for j, day in schedule.items():
                for i, class_ in day.items():
                    if class_['name'] is None: continue
                    class_obj.append(
                        Class(
                            idClasses = count_class,
                            timeClasses = date_TimeClass[int(i)].idTimeClasses,
                            dayWeek = date_DayWeeks[j].idDayWeek,
                            typeWeek = date_TypeWeek[index_week].idTypeWeek,
                            subjects = subjects_obj[class_['name']].idSubject,
                            idGroup = groups_obj[had].idGroup
                        )
                    )

                    for t in class_['teachers']:
                        key_teachers = f"{t['name']} {t['surname']} {t['patronymic']}"
                        TeachersClass_obj.append(
                            TeachersClass(
                                idTeacherClasses = count_TeachersClass,
                                idTeacher = teachers_obj[key_teachers].idTeacher,
                                idClass = class_obj[count_class].idClasses,
                                idClassrooms = classrooms_obj[t['classroom']['name']].idClassroom,

                            )
                        )
                        count_TeachersClass += 1


                    count_class += 1
        
        for group_ in data:
            await gen_class(group_['schedule_denominator'], 1, group_['hender'])
            await gen_class(group_['schedule_numerator'], 2, group_['hender'])
            
        return {
            'teachers_obj' : teachers_obj,
            'classrooms_obj' : classrooms_obj,
            'groups_obj' : groups_obj,
            'subjects_obj' : subjects_obj,
            'class_obj' : class_obj,
            'TeachersClass_obj' : TeachersClass_obj,
        }
            
    async def get_disciplines(data):

        disciplines = {}
        count = 0 

        async def gen_class(schedule, ):
            nonlocal count
            
            for day in schedule.values():
                for class_ in day.values():            
                    if  class_['teachers'] is None: continue
                    for t in class_['teachers']:
                        for di in t['disciplines']:
                            
                            if disciplines.get(di, None) == None:
                                disciplines[di] = count
                                count += 1
        
        for group in data:
            await gen_class(group['schedule_denominator'])
            await gen_class(group['schedule_numerator'])

        return disciplines 

    async def get_classroom(data):
        classroom_name = {}

        count = 0 

        async def gen_class(schedule, ):
            nonlocal count
            
            for day in schedule.values():
                for class_ in day.values():            
                    if  class_['teachers'] is None: continue
                    for t in class_['teachers']: 
                        if classroom_name.get(t['classroom']['name'], None) == None:
                            classroom_name[t['classroom']['name']] = count
                            count += 1
        
        

        for group in data:
            await gen_class(group['schedule_denominator'])
            await gen_class(group['schedule_numerator'])

        return classroom_name

    async def get_group(data):
        group_name = {}

        count = 0

        for group in data:
            if group_name.get(group['hender'], None) == None:
               group_name[group['hender']] = count
               count += 1

        return group_name

    async def get_class(data):
        class_name = {}
       
        count = 0 

        async def gen_class(schedule, ):
            nonlocal count
            
            for day in schedule.values():
                for class_ in day.values(): 

                    if class_name.get(class_['name'], None) == None:
                        class_name[class_['name']] = count
                        count += 1
        
        

        for group in data:
            await gen_class(group['schedule_denominator'])
            await gen_class(group['schedule_numerator'])

        return class_name

    async def insert_date(data):
        async with async_session_maker() as session:
            session.add_all(data)
            await session.commit()


    async def get_data(self,):
        with open(self.path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
            return data
        
    
        




















            