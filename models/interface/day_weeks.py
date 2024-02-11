from pydantic import BaseModel

class DayWeeksBase(BaseModel):
    Name: str    
    WeekEnd: bool

    class Config:
        from_attributes = True

class DayWeeksCreate(DayWeeksBase): ...

class DayWeeks(DayWeeksBase):
    idDayWeek: int
    


    
