from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.models.base import Base

class City(Base):
    """Модель для городов."""
    __tablename__ = "cities"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)

    # Связь с пользователями
    # users: Mapped[list["User"]] = relationship(back_populates="city", lazy="selectin")