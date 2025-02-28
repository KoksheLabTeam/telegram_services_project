from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.core.schemas.offer import OfferCreate, OfferUpdate, OfferResponse
from app.core.services.offer import OfferService
from app.core.database.helper import get_session

router = APIRouter(prefix="/offers", tags=["offers"])


def get_offer_service(session: Session = Depends(get_session)):
    return OfferService(session)


@router.post("/", response_model=OfferResponse)
def create_offer(offer_data: OfferCreate, service: OfferService = Depends(get_offer_service)):
    return service.create(offer_data)


@router.get("/{offer_id}", response_model=OfferResponse)
def get_offer(offer_id: int, service: OfferService = Depends(get_offer_service)):
    offer = service.get_by_id(offer_id)
    if not offer:
        raise HTTPException(status_code=404, detail="Offer not found")
    return offer


@router.put("/{offer_id}", response_model=OfferResponse)
def update_offer(offer_id: int, offer_data: OfferUpdate, service: OfferService = Depends(get_offer_service)):
    return service.update(offer_id, offer_data)


@router.delete("/{offer_id}")
def delete_offer(offer_id: int, service: OfferService = Depends(get_offer_service)):
    service.delete(offer_id)
    return {"detail": "Offer deleted successfully"}
