from app.core.schemas.base import BaseSchema
from typing import Optional
from datetime import datetime

class OfferRead(BaseSchema):
    id: int
    customer_id: int  # ID заказчика
    executor_id: int   # ID исполнителя
    order_id: int      # ID заказа
    price: float
    status: str
    created_at: datetime

class OfferCreate(BaseSchema):
    customer_id: int
    executor_id: int
    order_id: int
    price: float
    status: str

class OfferUpdate(BaseSchema):
    price: Optional[float] = None
    status: Optional[str] = None
