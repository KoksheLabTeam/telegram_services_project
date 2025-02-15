from sqlalchemy import ForeignKey, String, Text, TIMESTAMP
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from typing import Optional
from app.core.models.base import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    telegram_id: Mapped[int] = mapped_column(unique=True, nullable=False) # ID телеграм
    username: Mapped[str] = mapped_column(String(255), unique=True, nullable=True)  # Имя в Телеграм
    name: Mapped[str] = mapped_column(String(255), nullable=False)  # Имя пользователя
    is_customer: Mapped[bool] = mapped_column(default=False)  # Флаг заказчика
    is_executor: Mapped[bool] = mapped_column(default=True)  # Флаг исполнителя
    is_admin: Mapped[bool] = mapped_column(default=False)  # Флаг администратора
    city: Mapped[Optional[str]] = mapped_column(nullable=True)  # Город
    rating: Mapped[float] = mapped_column(default=0.0)  # Рейтинг
    completed_orders: Mapped[int] = mapped_column(default=0)  # Количество выполненных заказов





