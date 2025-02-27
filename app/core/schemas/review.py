from app.core.schemas.base import BaseSchema
from typing import Optional
from datetime import datetime

class ReviewRead(BaseSchema):
    id: int
    author_id: int
    target_id: int
    rating: int
    comment: Optional[str] = None
    created_at: datetime

class ReviewCreate(BaseSchema):
    author_id: int
    target_id: int
    rating: int
    comment: Optional[str] = None

class ReviewUpdate(BaseSchema):
    rating: Optional[int] = None
    comment: Optional[str] = None
