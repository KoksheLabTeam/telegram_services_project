from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.models.offer import Offer, OfferStatus


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
        try:
            result = self.session.execute(query)
            offer = result.scalar_one_or_none()
            if offer is None:
                raise OfferNotFoundException(f"Offer with id '{offer_id}' not found")
            return offer
        except Exception as e:
            self.session.rollback()
            raise OfferNotFoundException(str(e))
