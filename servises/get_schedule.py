import os, sys

from models.schemes import(
    Class, TimeClass, DayWeeks, Base, TypeWeek, TokenType, Role, Subjects, Groups, TeachersClass, Teachers, Classrooms
)

from sqlalchemy.future import select

from sqlalchemy.ext.asyncio import AsyncSession

from typing import List

async def select_schedule(type_week: str, group: str, session: AsyncSession, skip: int = 0, limit: int = 100) -> List:
    stmt = (
        select(
            Class.idClasses,  
            TimeClass.idTimeClasses, TimeClass.number, TimeClass.beginTime, TimeClass.endTime, 
            DayWeeks.idDayWeek, DayWeeks.Name, DayWeeks.WeekEnd,  
            TypeWeek.idTypeWeek, TypeWeek.Name, 
            Subjects.idSubject, Subjects.Name,
            Teachers.idTeacher, Teachers.Surname, Teachers.Name, Teachers.Patronymic, Teachers.email, Teachers.phoneNumber, Teachers.portrait,
            Classrooms.idClassroom, Classrooms.Name, Classrooms.Building, Classrooms.vector
        )
        .select_from(Class)
            .join(Groups, Class.idGroup == Groups.idGroup)
            .join(TimeClass, Class.timeClasses == TimeClass.idTimeClasses)
            .join(DayWeeks, Class.dayWeek == DayWeeks.idDayWeek)
            .join(TypeWeek, Class.typeWeek == TypeWeek.idTypeWeek)
            .join(Subjects, Class.subjects == Subjects.idSubject)
            
            .join(TeachersClass, Class.idClasses == TeachersClass.idClass)
            .join(Teachers, TeachersClass.idTeacher == Teachers.idTeacher)
            .join(Classrooms, TeachersClass.idClassrooms == Classrooms.idClassroom)
        .where(Groups.name == group, TypeWeek.Name == type_week)
        .offset(skip).limit(limit))

    result = await session.execute(stmt)
    
    result = result.all()

    date = {}    

    for i in result:
        if date.get(i[0], None) is None:
            date[i[0]] = {
                'timeClass': {
                    'idTimeClasses': i[1],
                    'number': i[2],
                    'beginTime': i[3],
                    'endTime': i[4]                   
                },
                'dayWeeks': {
                    'idDayWeek': i[5],
                    'name': i[6],
                    'weekEnd': i[7],
                },
                'typeWeek': {
                    'idTypeWeek': i[8],
                    'name': i[9],
                },
                'subjects': {
                    'idSubject': i[10],
                    'Name': i[11]
                },
                'teachers':[
                    
                ]
            }  

        date[i[0]]['teachers'].append(
            {
                'teachers': {
                    'idTeacher': i[12], 
                    'surname': i[13], 
                    'name': i[14], 
                    'patronymic': i[15], 
                    'email': i[16], 
                    'phoneNumber': i[17], 
                    'portrait': i[18],
                },
                'class': {
                    'idClassroom': i[19], 
                    'name': i[20], 
                    'building': i[21], 
                    'vector': i[22]
                }
            }
        )
    
    return list(date.values())