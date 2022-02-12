
# test tables
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Table,
    UniqueConstraint,
)

from bot.db.session import Base

# test table 1
class Section(Base):
    __tablename__ = 'sections'
    uid = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    description = Column(String)
    timetable = Column(String)
    sport_type = Column(String)

    def __repr__(self) -> str:
        return f'Section {self.name} {self.uid}'

# test table 2
class User(Base):
    __tablename__ = 'users'

    uid = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    tg_user_name = Column(String, index=True)

    tel_number = Column(Integer, unique=True)
    mail = Column(String, unique=True)
    section = Column(Integer, ForeignKey(Section.uid))

    def __repr__(self) -> str:
        return f'User {self.name} {self.uid}'
