from sqlalchemy import BigInteger, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column

from db.base import Base, AbstractClass


class Channel(Base, AbstractClass):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(VARCHAR)
