from sqlalchemy import ForeignKey, String, Text, TIMESTAMP
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from typing import Optional
from app.core.models.base import Base
from typing import List, TYPE_CHECKING

class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)

    Category: Mapped[List["users"]] = relationship()  # вытаскивает автоматический