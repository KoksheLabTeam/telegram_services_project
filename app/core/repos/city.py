from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from app.core.models.city import City

class CityCreateException(Exception):
    """Raise exception when there is an error during city creation."""

class CityNotFoundException(Exception):
    """Raise exception when no city is found."""

class CityRepo:
    def __init__(self, session: Session) -> None:
        self.session = session

    def create(self, instance: City) -> City:
        self.session.add(instance)
        try:
            self.session.commit()
            self.session.refresh(instance)
            return instance
        except Exception as e:
            self.session.rollback()
            raise CityCreateException(str(e))

    def get_by_id(self, city_id: int) -> City:
        query = select(City).where(City.id == city_id)
        result = self.session.execute(query)
        city = result.scalar_one_or_none()
        if not city:
            raise CityNotFoundException(f"City with id '{city_id}' not found")
        return city

    def update(self, city_id: int, update_data: dict) -> City:
        query = (
            update(City)
            .where(City.id == city_id)
            .values(**update_data)
            .returning(City)
        )
        result = self.session.execute(query)
        self.session.commit()
        return result.scalar_one()

    def delete(self, city_id: int) -> None:
        query = delete(City).where(City.id == city_id)
        self.session.execute(query)
        self.session.commit()

    def select(self, **filters):
        query = select(City).filter_by(**filters)
        result = self.session.execute(query)
        return result.scalars().all()