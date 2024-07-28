from sqlalchemy.orm import DeclarativeBase, declared_attr, Session

from config import DatabaseConfig

session = Session(DatabaseConfig().db_url)


class Base(DeclarativeBase):
    @declared_attr
    def __tablename__(self) -> str:
        return self.__name__.lower() + 's'
