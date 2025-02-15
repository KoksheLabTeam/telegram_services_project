from sqlalchemy import ForeignKey, String, Text, TIMESTAMP
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from typing import Optional
from app.core.models.base import Base

class Offer(Base):
    __tablename__ = "offers"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"), nullable=False)  # ID заказа
    executor_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)  # ID исполнителя
    proposed_price: Mapped[float] = mapped_column(nullable=False)  # Предложенная цена
    estimated_time: Mapped[str] = mapped_column(String(255), nullable=False)  # Примерное время выполнения
    status: Mapped[str] = mapped_column(default="pending")  # Статус предложения
