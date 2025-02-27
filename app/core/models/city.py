from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.models.base import Base

class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)

    users = relationship("User", back_populates="city")
