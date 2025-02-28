from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.core.models.base import Base
from decimal import Decimal
from sqlalchemy import ForeignKey, Enum, Numeric
import enum

class OrderStatus(str, enum.Enum):
    """Статусы заказов."""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class Order(Base):
    """Модель для заказов."""
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    executor_id: Mapped[int | None] = mapped_column(ForeignKey("users.id"), nullable=True)
    city_id: Mapped[int] = mapped_column(ForeignKey("cities.id"), nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    status: Mapped[OrderStatus] = mapped_column(Enum(OrderStatus), default=OrderStatus.PENDING, nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow, nullable=False)

    # Связи
    customer: Mapped["User"] = relationship("User", foreign_keys="Order.customer_id", back_populates="orders_created")
    executor: Mapped["User"] = relationship("User", foreign_keys="Order.executor_id", back_populates="orders_executed")
    city: Mapped["City"] = relationship("City")
    category: Mapped["Category"] = relationship("Category")
    offers: Mapped[list["Offer"]] = relationship("Offer", back_populates="order", cascade="all, delete")
    reviews: Mapped[list["Review"]] = relationship("Review", cascade="all, delete")