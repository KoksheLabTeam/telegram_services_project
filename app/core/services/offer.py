from app.core.models.offer import Offer
from app.core.schemas.offer import OfferCreate, OfferUpdate
from app.core.repos.offer import OfferRepo, OfferCreateException, OfferNotFoundException
from fastapi import HTTPException


class OfferService:
    def __init__(self, repository: OfferRepo) -> None:
        self.repository = repository

    def create(self, data: OfferCreate) -> Offer:
        instance = Offer(
            order_id=data.order_id,
            executor_id=data.executor_id,
            price=data.price,
            estimated_time=data.estimated_time,
            status=data.status,
        )

        try:
            offer = self.repository.create(instance)
            return offer
        except OfferCreateException as e:
            raise HTTPException(status_code=500, detail=f"Error while creating offer: {e}")

    def get_by_id(self, offer_id: int) -> Offer:
        offer = self.repository.get_by_id(offer_id)
        if not offer:
            raise HTTPException(status_code=404, detail="Offer not found")
        return offer

    def update(self, offer_id: int, update_data: OfferUpdate) -> Offer:
        try:
            return self.repository.update(offer_id, update_data)
        except OfferNotFoundException:
            raise HTTPException(status_code=404, detail="Offer not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error while updating offer: {e}")

    def delete(self, offer_id: int) -> None:
        try:
            self.repository.delete(offer_id)
        except OfferNotFoundException:
            raise HTTPException(status_code=404, detail="Offer not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error while deleting offer: {e}")
