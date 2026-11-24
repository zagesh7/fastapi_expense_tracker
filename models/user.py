from core.database import Base
from datetime import datetime
from sqlalchemy import DateTime,func
from sqlalchemy.orm import Mapped,mapped_column

class User(Base):
    __tablename__="users"

    id:Mapped[int]=mapped_column(primary_key=True,index=True)
    username:Mapped[str]=mapped_column(unique=True)
    hashed_password:Mapped[str]
    created_at:Mapped[datetime]=mapped_column(DateTime,default=func.now())