from sqlalchemy import BigInteger, VARCHAR
from sqlalchemy.orm import mapped_column, Mapped, relationship

from db.base import Base, AbstractClass, article_author_association


class Movie(Base, AbstractClass):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(VARCHAR)
    movies = relationship('Genre', secondary=article_author_association, back_populates='authors', lazy='joined')