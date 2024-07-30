from sqlalchemy import BigInteger, VARCHAR, Table, Column, ForeignKey, TEXT
from sqlalchemy.orm import mapped_column, Mapped, relationship

from db.base import Base, AbstractClass

give_users = Table(
    "genre_movie",
    Base.metadata,
    Column('genre_id', ForeignKey('genres.id'), primary_key=True),
    Column('movie_id', ForeignKey('movies.id'), primary_key=True)
)


class User(Base, AbstractClass):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(VARCHAR)


class Movie(Base, AbstractClass):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(VARCHAR)
    description: Mapped[str] = mapped_column(TEXT)
    pixel: Mapped[str] = mapped_column(VARCHAR(10))
    genres = relationship('Genre', secondary=give_users, back_populates='movies')


class Genre(Base, AbstractClass):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(VARCHAR)
    movies = relationship('Movie', secondary=give_users, back_populates='genres')


class Channel(Base, AbstractClass):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(VARCHAR)
