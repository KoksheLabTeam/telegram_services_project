from fastapi import HTTPException
from app.core.models.offer import Offer
from app.core.schemas.offer import OfferCreate, OfferUpdate, OfferRead
from app.core.repos.offer import OfferRepo, OfferCreateException, OfferNotFoundException

class OfferService:
    def __init__(self, repository: OfferRepo) -> None:
        self.repository = repository

    def create(self, data: OfferCreate) -> OfferRead:
        instance = Offer(
            order_id=data.order_id,
            executor_id=data.executor_id,
            price=data.price,
            estimated_time=data.estimated_time,
            status=data.status,
        )
        try:
            offer = self.repository.create(instance)
            return OfferRead.from_orm(offer)
        except OfferCreateException as e:
            raise HTTPException(status_code=500, detail=f"Error while creating offer: {e}")

    def get_by_id(self, offer_id: int) -> OfferRead:
        try:
            offer = self.repository.get_by_id(offer_id)
            if not offer:
                raise HTTPException(status_code=404, detail="Offer not found")
            return OfferRead.from_orm(offer)
        except OfferNotFoundException:
            raise HTTPException(status_code=404, detail="Offer not found")

    def update(self, offer_id: int, update_data: OfferUpdate) -> OfferRead:
        try:
            offer = self.repository.update(offer_id, update_data.dict(exclude_unset=True))
            return OfferRead.from_orm(offer)
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

    def select(self, **filters):
        offers = self.repository.select(**filters)
        if not offers:
            raise HTTPException(status_code=404, detail="No offers found")
        return [OfferRead.from_orm(offer) for offer in offers]