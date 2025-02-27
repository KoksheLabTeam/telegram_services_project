from sqlalchemy import Column, Integer, ForeignKey, Table
from app.core.models.base import Base

user_categories = Table(
    "user_categories", Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("category_id", Integer, ForeignKey("categories.id"), primary_key=True)
)
