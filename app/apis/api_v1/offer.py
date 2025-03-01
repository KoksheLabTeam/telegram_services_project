from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List
from app.core.schemas.offer import OfferCreate, OfferUpdate, OfferRead  # Предполагаю, OfferResponse = OfferRead
from app.core.services.offer import OfferService
from app.core.repos.offer import OfferRepo
from app.core.database.helper import get_session

router = APIRouter(prefix="/offers", tags=["offers"])

def get_offer_service(session: Session = Depends(get_session)):
    return OfferService(OfferRepo(session))

def parse_filters(order_id: int = Query(None), executor_id: int = Query(None)) -> dict:
    filters = {}
    if order_id:
        filters["order_id"] = order_id
    if executor_id:
        filters["executor_id"] = executor_id
    return filters

@router.post("/", response_model=OfferRead)
def create_offer(offer_data: OfferCreate, service: OfferService = Depends(get_offer_service)):
    return service.create(offer_data)

@router.get("/{offer_id}", response_model=OfferRead)
def get_offer(offer_id: int, service: OfferService = Depends(get_offer_service)):
    return service.get_by_id(offer_id)

@router.put("/{offer_id}", response_model=OfferRead)
def update_offer(offer_id: int, offer_data: OfferUpdate, service: OfferService = Depends(get_offer_service)):
    return service.update(offer_id, offer_data)

@router.delete("/{offer_id}")
def delete_offer(offer_id: int, service: OfferService = Depends(get_offer_service)):
    service.delete(offer_id)
    return {"detail": "Offer deleted successfully"}

@router.get("/select/", response_model=List[OfferRead])
def select_offers(filters: dict = Depends(parse_filters), service: OfferService = Depends(get_offer_service)):
    return service.select(**filters)