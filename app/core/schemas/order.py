from app.core.schemas.base import BaseSchema
from typing import Optional
from datetime import datetime

class OrderCreate(BaseSchema):
    customer_id: int
    executor_id: Optional[int] = None
    category_id: int
    description: str
    status: str  # Например, "pending", "in_progress", "completed"
    created_at: datetime = datetime.utcnow()

class OrderUpdate(BaseSchema):
    executor_id: Optional[int] = None
    status: Optional[str] = None  # Изменяемый статус

class OrderResponse(BaseSchema):
    id: int
    customer_id: int
    executor_id: Optional[int]
    category_id: int
    description: str
    status: str
    created_at: datetime
