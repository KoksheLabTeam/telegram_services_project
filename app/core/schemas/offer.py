from app.core.schemas.base import BaseSchema
from typing import Optional
from datetime import datetime
from decimal import Decimal
from enum import Enum

class OfferStatus(str, Enum):
    PENDING = "pending"
    ACCEPTED = "accepted"
    REJECTED = "rejected"

class OfferCreate(BaseSchema):
    order_id: int
    executor_id: int
    price: Decimal
    estimated_time: int

class OfferUpdate(BaseSchema):
    price: Optional[Decimal] = None
    estimated_time: Optional[int] = None
    status: Optional[OfferStatus] = None

class OfferResponse(BaseSchema):
    id: int
    order_id: int
    executor_id: int
    price: Decimal
    estimated_time: int
    status: OfferStatus
    created_at: datetime