from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.core.models.base import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Numeric, Enum, CheckConstraint

class Review(Base):
    """Модель для отзывов."""
    __tablename__ = "reviews"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id", ondelete="CASCADE"), nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    target_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    rating: Mapped[int] = mapped_column(CheckConstraint("rating BETWEEN 1 AND 5"), nullable=False)
    comment: Mapped[str | None] = mapped_column(nullable=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow, nullable=False)

    # Связи
    order: Mapped["Order"] = relationship("Order")
    # author: Mapped["User"] = relationship( back_populates="reviews_written", lazy='selectin')
    # target: Mapped["User"] = relationship( back_populates="reviews_received", lazy='selectin')