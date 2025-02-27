from app.core.schemas.base import BaseSchema
from typing import Optional

class UserCategoryRead(BaseSchema):
    id: int
    user_id: int
    category_id: int

class UserCategoryCreate(BaseSchema):
    user_id: int
    category_id: int

class UserCategoryUpdate(BaseSchema):
    user_id: Optional[int] = None
    category_id: Optional[int] = None
