from datetime import datetime
from sqlalchemy.sql import func

from sqlalchemy import Enum, ForeignKey, BIGINT, SMALLINT, TEXT, DateTime, Integer, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase, declared_attr, Session


session = Session(DB.engine)


class Base(DeclarativeBase):

    @declared_attr
    def __tablename__(self) -> str:
        return self.__name__.lower() + 's'
