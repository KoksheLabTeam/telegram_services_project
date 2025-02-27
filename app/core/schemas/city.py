from app.core.schemas.base import BaseSchema
from typing import Optional

class CityRead(BaseSchema):
    id: int
    name: str


class CityCreate(BaseSchema):
    name: str


class CityUpdate(BaseSchema):
    name: Optional[str] = None
