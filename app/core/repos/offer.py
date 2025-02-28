from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from app.core.models.offer import Offer

class OfferCreateException(Exception):
    """Raise exception when there is an error during offer creation."""

class OfferNotFoundException(Exception):
    """Raise exception when no offer is found."""

class OfferRepo:
    def __init__(self, session: Session) -> None:
        self.session = session

    def create(self, instance: Offer) -> Offer:
        self.session.add(instance)
        try:
            self.session.commit()
            self.session.refresh(instance)
            return instance
        except Exception as e:
            self.session.rollback()
            raise OfferCreateException(str(e))

    def get_by_id(self, offer_id: int) -> Offer:
        query = select(Offer).where(Offer.id == offer_id)
        result = self.session.execute(query)
        offer = result.scalar_one_or_none()
        if not offer:
            raise OfferNotFoundException(f"Offer with id '{offer_id}' not found")
        return offer

    def update(self, offer_id: int, update_data: dict) -> Offer:
        query = (
            update(Offer)
            .where(Offer.id == offer_id)
            .values(**update_data)
            .returning(Offer)
        )
        result = self.session.execute(query)
        self.session.commit()
        return result.scalar_one()

    def delete(self, offer_id: int) -> None:
        query = delete(Offer).where(Offer.id == offer_id)
        self.session.execute(query)
        self.session.commit()

    def select(self, **filters):
        query = select(Offer).filter_by(**filters)
        result = self.session.execute(query)
        return result.scalars().all()