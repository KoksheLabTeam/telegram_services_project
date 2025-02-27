from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from app.core.models.base import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(Integer, unique=True, nullable=False)
    name = Column(String, nullable=False)
    username = Column(String, unique=True, nullable=True)
    is_customer = Column(Boolean, default=False)
    is_executor = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)  # Скрытый, виден только админу
    city_id = Column(Integer, ForeignKey("cities.id", ondelete="CASCADE"), nullable=False)
    rating = Column(Numeric(2, 1), default=0.0)
    completed_orders = Column(Integer, default=0)

    city = relationship("City", back_populates="users")
    categories = relationship("Category", secondary="user_categories", back_populates="users")
    orders_created = relationship("Order", foreign_keys="[Order.customer_id]", back_populates="customer")
    orders_executed = relationship("Order", foreign_keys="[Order.executor_id]", back_populates="executor")
    offers = relationship("Offer", back_populates="executor", cascade="all, delete")
    reviews_received = relationship("Review", foreign_keys="[Review.target_id]", back_populates="target", cascade="all, delete")
    reviews_written = relationship("Review", foreign_keys="[Review.author_id]", back_populates="author", cascade="all, delete")
