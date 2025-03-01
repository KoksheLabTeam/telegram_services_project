from app.core.schemas.base import BaseSchema
from typing import Optional, List

class UserRead(BaseSchema):
    """Схема для чтения пользователя."""
    id: int
    telegram_id: int
    name: str
    username: Optional[str] = None
    is_customer: bool
    is_executor: bool
    is_admin: bool
    city_id: int
    rating: float
    completed_orders: int

class UserCreate(BaseSchema):
    """Схема для создания пользователя."""
    telegram_id: int
    name: str
    username: Optional[str] = None
    is_customer: bool = False
    is_executor: bool = True
    is_admin: bool = False
    city_id: int
    rating: float = 0.0
    completed_orders: int = 0

class UserUpdate(BaseSchema):
    name: Optional[str] = None
    username: Optional[str] = None
    is_customer: Optional[bool] = None
    is_executor: Optional[bool] = None
    is_admin: Optional[bool] = None
    city_id: Optional[int] = None
    rating: Optional[float] = None
    completed_orders: Optional[int] = None
    categories: Optional[List[int]] = None  # ID категорий