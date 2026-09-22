from sqlalchemy import String, Integer

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

'''
This file is the lowest layer in development, this class user is used to map in database how User entity will be formated.
'''


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(30), nullable=False)

    def __repr__(self):
        return f"User(id={self.id!r}, email={self.email!r})"