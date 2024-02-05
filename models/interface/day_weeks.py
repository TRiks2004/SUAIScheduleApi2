from pydantic import BaseModel

class DayWeeksBase(BaseModel):
    Name: str    
    WekEnd: bool

    class Config:
        orm_mode = True

class DayWeeksCreate(DayWeeksBase): ...

class DayWeeks(DayWeeksBase):
    idDayWeek: int
    


    
