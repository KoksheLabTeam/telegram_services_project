from app.core.schemas.base import BaseSchema
from typing import Optional
from datetime import datetime

class ReviewRead(BaseSchema):
    """Схема для чтения отзыва."""
    id: int
    order_id: int
    author_id: int
    target_id: int
    rating: int
    comment: Optional[str] = None
    created_at: datetime

class ReviewCreate(BaseSchema):
    """Схема для создания отзыва."""
    order_id: int
    author_id: int
    target_id: int
    rating: int
    comment: Optional[str] = None

class ReviewUpdate(BaseSchema):
    """Схема для обновления отзыва."""
    rating: Optional[int] = None
    comment: Optional[str] = None