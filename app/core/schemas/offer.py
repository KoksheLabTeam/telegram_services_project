from app.core.schemas.base import BaseSchema
from typing import Optional
from datetime import datetime
from decimal import Decimal
from enum import Enum

class OfferStatus(str, Enum):
    """Статусы предложений."""
    PENDING = "pending"
    ACCEPTED = "accepted"
    REJECTED = "rejected"

class OfferRead(BaseSchema):
    """Схема для чтения предложения."""
    id: int
    order_id: int
    executor_id: int
    price: Decimal
    estimated_time: int
    status: OfferStatus
    created_at: datetime

class OfferCreate(BaseSchema):
    """Схема для создания предложения."""
    order_id: int
    executor_id: int
    price: Decimal
    estimated_time: int
    status: OfferStatus = OfferStatus.PENDING

class OfferUpdate(BaseSchema):
    """Схема для обновления предложения."""
    price: Optional[Decimal] = None
    estimated_time: Optional[int] = None
    status: Optional[OfferStatus] = None