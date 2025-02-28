from sqlalchemy import select
from sqlalchemy.orm import Session
from app.core.schemas.offer import OfferResponse
from app.core.models.offer import Offer, OfferStatus


class OfferCreateException(Exception):
    """Raise exception when there is an error during offer creation."""


class OfferNotFoundException(Exception):
    """Raise exception when no offer is found."""


class OfferRepo:
    def __init__(self, session: Session) -> None:
        self.session = session

    def create(self, instance: Offer) -> OfferResponse:
        self.session.add(instance)
        try:
            self.session.commit()
            self.session.refresh(instance)
            return OfferResponse.model_validate(instance)
        except Exception as e:
            self.session.rollback()
            raise OfferCreateException(str(e))

    def get_by_id(self, offer_id: int) -> Offer:
        query = select(Offer).where(Offer.id == offer_id)
        try:
            result = self.session.execute(query).scalar_one_or_none()
            if not result:
                raise OfferNotFoundException(f"Offer with id '{offer_id}' not found")
            return OfferResponse.model_validate(result)
        except Exception as e:
            self.session.rollback()
            raise OfferNotFoundException(str(e))
