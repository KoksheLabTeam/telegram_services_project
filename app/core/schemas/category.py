from app.core.schemas.base import BaseSchema
from typing import Optional

class CategoryRead(BaseSchema):
    """Схема для чтения категории."""
    id: int
    name: str

class CategoryCreate(BaseSchema):
    """Схема для создания категории."""
    name: str

class CategoryUpdate(BaseSchema):
    """Схема для обновления категории."""
    name: Optional[str] = None