from app.core.schemas.base import BaseSchema
from typing import Optional

class UserRead(BaseSchema):
    id: int
    telegram_id: int
    name: str
    username: Optional[str] = None
    city_id: int
    rating: float
    completed_orders: int

class UserCreate(BaseSchema):
    telegram_id: int
    name: str
    username: Optional[str] = None
    city_id: int

class UserUpdate(BaseSchema):
    name: Optional[str] = None
    username: Optional[str] = None
    city_id: Optional[int] = None

class UserResponse(BaseSchema):
    id: int
    telegram_id: int
    name: str
    username: Optional[str]
    is_customer: bool
    is_executor: bool
    is_admin: bool
    city_id: int
    rating: float
    completed_orders: int