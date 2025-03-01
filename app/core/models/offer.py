from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.core.models.base import Base
from decimal import Decimal
from sqlalchemy import Column, ForeignKey, Integer, String, Numeric, Enum  # Добавлен Enum
import enum

class OfferStatus(str, enum.Enum):
    """Статусы предложений."""
    PENDING = "pending"
    ACCEPTED = "accepted"
    REJECTED = "rejected"

class Offer(Base):
    """Модель для предложений."""
    __tablename__ = "offers"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id", ondelete="CASCADE"), nullable=False)
    executor_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    estimated_time: Mapped[int] = mapped_column(nullable=False)
    status: Mapped[OfferStatus] = mapped_column(Enum(OfferStatus), default=OfferStatus.PENDING, nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow, nullable=False)

    # # Связи
    # order: Mapped["Order"] = relationship("Order", back_populates="offers")
    # executor: Mapped["User"] = relationship("User", back_populates="offers")