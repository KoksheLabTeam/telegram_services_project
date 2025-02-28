from app.core.schemas.base import BaseSchema
from typing import Optional

class CityRead(BaseSchema):
    """Схема для чтения города."""
    id: int
    name: str

class CityCreate(BaseSchema):
    """Схема для создания города."""
    name: str

class CityUpdate(BaseSchema):
    """Схема для обновления города."""
    name: Optional[str] = None