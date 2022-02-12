
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

<<<<<<< HEAD

class SectionType(Base):
    __tablename__ = 'section_type'
    uid = Column(Integer, primary_key=True)
    name = Column(String, index=True, unique=True)

    def __repr__(self) -> str:
        return f'SectionType {self.name} {self.uid}'

class AgeGroup(Base):
    __tablename__ = 'age_group'
    uid = Column(Integer, primary_key=True)
    name = Column(String, index=True)

    def __repr__(self) -> str:
        return f'AgeGroup {self.name} {self.uid}'


=======
# test table 1
>>>>>>> 88d2b3517cdafb74f96b881ac4708ed45da46f1e
class Section(Base):
    __tablename__ = 'sections'
    uid = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    description = Column(String)
    timetable = Column(String)
    sport_type = Column(Integer, ForeignKey(SectionType.uid))

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
