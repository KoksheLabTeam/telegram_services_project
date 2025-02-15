from app.core.models.base import Base

from sqlalchemy.orm import Mapped, mapped_column

from sqlalchemy import ForeignKey

class User(Base):
    __tablename__ = "users"

    name: Mapped[str] = mapped_column(unique=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))