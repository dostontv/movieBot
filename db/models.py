from sqlalchemy import BigInteger, VARCHAR
from sqlalchemy.orm import mapped_column, Mapped

from db.base import Base, AbstractClass


class User(Base, AbstractClass):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(VARCHAR)


class Movie(Base, AbstractClass):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(VARCHAR)
    pixel: Mapped[str] = mapped_column(VARCHAR(10))
    size: Mapped[str] = mapped_column(VARCHAR(10))


class Channel(Base, AbstractClass):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(VARCHAR)
