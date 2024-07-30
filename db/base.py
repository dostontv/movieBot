from sqlalchemy.orm import DeclarativeBase, declared_attr, Session

from config import DatabaseConfig, conf

from sqlalchemy import delete as sqlalchemy_delete, update as sqlalchemy_update, Table, Column, Integer, ForeignKey
from sqlalchemy.future import select

session = Session(conf.db.db_url)


class Base(DeclarativeBase):
    @declared_attr
    def __tablename__(self) -> str:
        return self.__name__.lower() + 's'


class AbstractClass:
    @staticmethod
    def commit():
        try:
            session.commit()
        except Exception:
            session.rollback()
            raise

    @classmethod
    def create(cls, **kwargs):  # Create
        object_ = cls(**kwargs)
        session.add(object_)
        cls.commit()
        return object_

    @classmethod
    def update(cls, id_, **kwargs):
        query = (
            sqlalchemy_update(cls)
            .where(cls.id == id_)
            .values(**kwargs)
            .execution_options(synchronize_session="fetch")
        )
        session.execute(query)
        cls.commit()

    @classmethod
    def get(cls, id_):
        query = select(cls).where(cls.id == id_)
        return (session.execute(query)).scalar()

    @classmethod
    def delete(cls, id_):
        query = sqlalchemy_delete(cls).where(cls.id == id_)
        session.execute(query)
        cls.commit()

    @classmethod
    def get_all(cls):
        return (session.execute(select(cls))).scalars()

