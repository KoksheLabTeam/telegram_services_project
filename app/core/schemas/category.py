from app.core.schemas.base import BaseSchema
from typing import Optional

class CategoryRead(BaseSchema):
    id: int
    name: str


class CategoryCreate(BaseSchema):
    name: str


class CategoryUpdate(BaseSchema):
    name: Optional[str] = None
