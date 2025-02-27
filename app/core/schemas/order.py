from app.core.schemas.base import BaseSchema
from typing import Optional
from datetime import datetime

class OrderRead(BaseSchema):
    id: int
    customer_id: int
    title: str
    description: Optional[str] = None
    price: float
    status: str
    created_at: datetime

class OrderCreate(BaseSchema):
    customer_id: int
    title: str
    description: Optional[str] = None
    price: float
    status: str

class OrderUpdate(BaseSchema):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    status: Optional[str] = None
