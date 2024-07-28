from sqlalchemy import BigInteger, VARCHAR
from sqlalchemy.orm import mapped_column, Mapped

from db.base import CreatedModel


class User(CreatedModel):
    user_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(VARCHAR)
