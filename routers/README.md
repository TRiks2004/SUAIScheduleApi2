# Routers
## Default Values
### Time Class(`http://host:port/default/timeclass?skip=0&limit=100`)
```python
@router_default.get("/timeclass", response_model=List[TimeClass])
async def get_timeclass(
    skip: int = 0, limit: int = 100, 
    session: AsyncSession = Depends(get_async_session)) -> List[TimeClass]:
    ...
```

> returns: List[TimeClass]
> 
**Example:**

![alt text](https://drive.google.com/uc?id=1MYUpciZeRMUsaVZNE553w8WYoH4rTt0z) 
---




