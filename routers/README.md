# Routers
## Default Values
### get_timeclass(`http://host:port/default/timeclass?skip=0&limit=100`)
```python
@router_default.get("/timeclass", response_model=List[TimeClass])
async def get_timeclass(
    skip: int = 0, limit: int = 100, 
    session: AsyncSession = Depends(get_async_session)) -> List[TimeClass]:
    ...
```

> returns: List[TimeClass]

**Example:**

![Example get_timeclass](https://drive.google.com/uc?id=1MYUpciZeRMUsaVZNE553w8WYoH4rTt0z) 
---

### get_timeclass_by_number(`http://host:port/default/timeclass/{number}`)
```python
@router_default.get("/timeclass/{number}", response_model=TimeClass)
async def get_timeclass_by_number(
    number: int, 
    session: AsyncSession = Depends(get_async_session)) -> TimeClass:
    ...
```

> returns: TimeClass

**Example:**

![Example get_timeclass_by_number](https://drive.google.com/uc?id=1xOJDG9hQVvcDEsjMg23swHJ2jZS4eJm5)


