from sqlalchemy import Column, ForeignKey, Table
from app.core.models.base import Base

user_categories = Table(
    "user_categories", Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("category_id", ForeignKey("categories.id"), primary_key=True)
)