from app.core.schemas.base import BaseSchema
from typing import Optional

class UserCategoryRead(BaseSchema):
    """Схема для чтения связи пользователя и категории."""
    id: int
    user_id: int
    category_id: int

class UserCategoryCreate(BaseSchema):
    """Схема для создания связи пользователя и категории."""
    user_id: int
    category_id: int

class UserCategoryUpdate(BaseSchema):
    """Схема для обновления связи пользователя и категории."""
    user_id: Optional[int] = None
    category_id: Optional[int] = None