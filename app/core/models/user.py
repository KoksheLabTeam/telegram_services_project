from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional
from app.core.models.base import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    telegram_id: Mapped[int] = mapped_column(unique=True, nullable=False) # ID телеграм
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=True)  # Имя в Телеграм
    first_name: Mapped[str] = mapped_column(String(50))  # Имя пользователя
    last_name: Mapped[str] = mapped_column(String(50))  # Имя пользователя
    is_customer: Mapped[bool] = mapped_column(default=False)  # Флаг заказчика
    is_executor: Mapped[bool] = mapped_column(default=True)  # Флаг исполнителя
    is_admin: Mapped[bool] = mapped_column(default=False)  # Флаг администратора
    city: Mapped[Optional[str]] = mapped_column(nullable=True)  # Город
    rating: Mapped[float] = mapped_column(default=0.0)  # Рейтинг
    completed_orders: Mapped[int] = mapped_column(default=0)  # Количество выполненных заказов





