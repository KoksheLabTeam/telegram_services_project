from sqlalchemy import ForeignKey, Text, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional
from app.core.models.base import Base

class Review(Base):
    __tablename__ = "reviews"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"), nullable=False)  # ID заказа
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)  # ID автора отзыва
    target_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)  # ID получателя отзыва
    rating: Mapped[int] = mapped_column(nullable=False)  # Оценка (от 1 до 5)
    comment: Mapped[Optional[str]] = mapped_column(Text, nullable=True)  # Комментарий к отзыву
    created_at: Mapped[TIMESTAMP] = mapped_column(server_default="CURRENT_TIMESTAMP")  # Время создания