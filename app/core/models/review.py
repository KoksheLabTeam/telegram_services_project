from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, CheckConstraint
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.models.base import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id", ondelete="CASCADE"), nullable=False)
    author_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)  # Кто оставил отзыв
    target_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)  # Кому отзыв
    rating = Column(Integer, CheckConstraint("rating BETWEEN 1 AND 5"), nullable=False)
    comment = Column(String, nullable=True)  # Текст отзыва
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    order = relationship("Order")
    author = relationship("User", foreign_keys="Review.author_id", back_populates="reviews_written")
    target = relationship("User", foreign_keys="Review.target_id", back_populates="reviews_received")