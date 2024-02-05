
from pydantic import BaseModel

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

class NewsBase(BaseModel):
    ...

    class Config:
        orm_mode = True

class NewsCreate(NewsBase):
    ...

class News(NewsBase):
    ...
