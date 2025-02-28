from app.core.schemas.base import BaseSchema
from typing import Optional
from datetime import datetime
from decimal import Decimal
from enum import Enum

class OrderStatus(str, Enum):
    """Статусы заказов."""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class OrderRead(BaseSchema):
    """Схема для чтения заказа."""
    id: int
    customer_id: int
    executor_id: Optional[int]
    city_id: int
    category_id: int
    description: str
    price: Decimal
    status: OrderStatus
    created_at: datetime

class OrderCreate(BaseSchema):
    """Схема для создания заказа."""
    customer_id: int
    executor_id: Optional[int] = None
    city_id: int
    category_id: int
    description: str
    price: Decimal
    status: OrderStatus = OrderStatus.PENDING

class OrderUpdate(BaseSchema):
    """Схема для обновления заказа."""
    executor_id: Optional[int] = None
    status: Optional[OrderStatus] = None