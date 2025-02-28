from fastapi import HTTPException
from app.core.models.city import City
from app.core.schemas.city import CityCreate, CityUpdate, CityRead
from app.core.repos.city import CityRepo, CityCreateException, CityNotFoundException

class CityService:
    def __init__(self, repository: CityRepo) -> None:
        self.repository = repository

    def create(self, data: CityCreate) -> CityRead:
        instance = City(name=data.name)
        try:
            city = self.repository.create(instance)
            return CityRead.from_orm(city)
        except CityCreateException as e:
            raise HTTPException(status_code=500, detail=f"Error while creating city: {e}")

    def get_by_id(self, city_id: int) -> CityRead:
        try:
            city = self.repository.get_by_id(city_id)
            if not city:
                raise HTTPException(status_code=404, detail="City not found")
            return CityRead.from_orm(city)
        except CityNotFoundException:
            raise HTTPException(status_code=404, detail="City not found")

    def update(self, city_id: int, update_data: CityUpdate) -> CityRead:
        try:
            city = self.repository.update(city_id, update_data.dict(exclude_unset=True))
            return CityRead.from_orm(city)
        except CityNotFoundException:
            raise HTTPException(status_code=404, detail="City not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error while updating city: {e}")

    def delete(self, city_id: int) -> None:
        try:
            self.repository.delete(city_id)
        except CityNotFoundException:
            raise HTTPException(status_code=404, detail="City not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error while deleting city: {e}")

    def select(self, **filters):
        cities = self.repository.select(**filters)
        if not cities:
            raise HTTPException(status_code=404, detail="No cities found")
        return [CityRead.from_orm(city) for city in cities]