from sqlalchemy import Column, Integer, String, ForeignKey, Enum, DateTime, Numeric
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.models.base import Base
import enum

class OrderStatus(str, enum.Enum):
    PENDING = "pending"          # В ожидании исполнителя
    IN_PROGRESS = "in_progress"  # В процессе выполнения
    COMPLETED = "completed"      # Завершён
    CANCELLED = "cancelled"      # Отменён

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    executor_id = Column(Integer, ForeignKey("users.id"), nullable=True)  # Может быть NULL, пока не назначен
    city_id = Column(Integer, ForeignKey("cities.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    description = Column(String, nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    status = Column(Enum(OrderStatus), default=OrderStatus.PENDING, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    customer = relationship("User", foreign_keys="Order.customer_id", back_populates="orders_created")
    executor = relationship("User", foreign_keys="Order.executor_id", back_populates="orders_executed")
    city = relationship("City")
    category = relationship("Category")
    offers = relationship("Offer", back_populates="order", cascade="all, delete")
    reviews = relationship("Review", cascade="all, delete")
