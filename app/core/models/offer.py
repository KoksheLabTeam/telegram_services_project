from sqlalchemy import Column, Integer, ForeignKey, Enum, DateTime, Numeric
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.models.base import Base
import enum

class OfferStatus(str, enum.Enum):
    PENDING = "pending"          # Ожидание ответа заказчика
    ACCEPTED = "accepted"        # Принято заказчиком
    REJECTED = "rejected"        # Отклонено заказчиком

class Offer(Base):
    __tablename__ = "offers"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id", ondelete="CASCADE"), nullable=False)
    executor_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    price = Column(Numeric(10, 2), nullable=False)  # Цена, предложенная исполнителем
    estimated_time = Column(Integer, nullable=False)  # Оценка времени (в часах или днях)
    status = Column(Enum(OfferStatus), default=OfferStatus.PENDING, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    order = relationship("Order", back_populates="offers")
    executor = relationship("User", back_populates="offers")
