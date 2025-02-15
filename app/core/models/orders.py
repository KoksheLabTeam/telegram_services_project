from sqlalchemy import ForeignKey, String, Text, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column
from app.core.models.base import Base

class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)  # ID заказчика
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), nullable=False)  # ID категории
    description: Mapped[str] = mapped_column(Text, nullable=False)  # Описание заказа
    price: Mapped[float] = mapped_column(nullable=False)  # Предложенная цена
    city: Mapped[str] = mapped_column(String(255), nullable=False)  # Город заказа
    created_at: Mapped[TIMESTAMP] = mapped_column(server_default="CURRENT_TIMESTAMP")  # Время создания
    status: Mapped[str] = mapped_column(default="open")  # Статус заказа