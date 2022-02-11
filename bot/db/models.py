from bot.db.session import create_db
from typing import Any

from flask_sqlalchemy import SQLAlchemy
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
from sqlalchemy.orm import relationship

from bot.db.session import Base


class Section(Base):

    __tablename__ = 'sections'
    uid = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    description = Column(String)
    timetable = Column(String)
    sport_type = Column(String)

    def __repr__(self) -> str:
        return f'Section {self.name} {self.uid}'


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


if __name__ == '__main__':
    create_db()
