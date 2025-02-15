from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.core.models.base import Base

class ExecutorCategory(Base):
    __tablename__ = "executor_categories"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    executor_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)  # ID исполнителя
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), nullable=False)  # ID категории
