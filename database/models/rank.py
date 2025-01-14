from sqlalchemy import Column, Integer
from database.orm import Base


class UserRank(Base):
    __tablename__ = 'user_rank'

    user_id = Column('user_id', Integer, primary_key=True)
    points = Column('points', Integer, nullable=False)
