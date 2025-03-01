from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.core.schemas.city import CityCreate, CityUpdate, CityRead
from app.core.services.city import CityService
from app.core.repos.city import CityRepo
from app.core.database.helper import get_session

router = APIRouter(prefix="/cities", tags=["cities"])

def parse_filters(name: str = Query(None)) -> dict:
    filters = {}
    if name:
        filters["name"] = name
    return filters

@router.post("/", response_model=CityRead)
def create_city(city: CityCreate, db: Session = Depends(get_session)):
    service = CityService(CityRepo(db))
    return service.create(city)

@router.get("/{city_id}", response_model=CityRead)
def get_city(city_id: int, db: Session = Depends(get_session)):
    service = CityService(CityRepo(db))
    return service.get_by_id(city_id)

@router.put("/{city_id}", response_model=CityRead)
def update_city(city_id: int, city: CityUpdate, db: Session = Depends(get_session)):
    service = CityService(CityRepo(db))
    return service.update(city_id, city)

@router.delete("/{city_id}")
def delete_city(city_id: int, db: Session = Depends(get_session)):
    service = CityService(CityRepo(db))
    service.delete(city_id)
    return {"detail": "City deleted successfully"}

@router.get("/select/", response_model=list[CityRead])
def select_cities(filters: dict = Depends(parse_filters), db: Session = Depends(get_session)):
    service = CityService(CityRepo(db))
    return service.select(**filters)