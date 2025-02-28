from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from app.core.models.review import Review

class ReviewCreateException(Exception):
    """Raise exception when there is an error during review creation."""

class ReviewNotFoundException(Exception):
    """Raise exception when no review is found."""

class ReviewRepo:
    def __init__(self, session: Session) -> None:
        self.session = session

    def create(self, instance: Review) -> Review:
        self.session.add(instance)
        try:
            self.session.commit()
            self.session.refresh(instance)
            return instance
        except Exception as e:
            self.session.rollback()
            raise ReviewCreateException(str(e))

    def get_by_id(self, review_id: int) -> Review:
        query = select(Review).where(Review.id == review_id)
        result = self.session.execute(query)
        review = result.scalar_one_or_none()
        if not review:
            raise ReviewNotFoundException(f"Review with id '{review_id}' not found")
        return review

    def update(self, review_id: int, update_data: dict) -> Review:
        query = (
            update(Review)
            .where(Review.id == review_id)
            .values(**update_data)
            .returning(Review)
        )
        result = self.session.execute(query)
        self.session.commit()
        return result.scalar_one()

    def delete(self, review_id: int) -> None:
        query = delete(Review).where(Review.id == review_id)
        self.session.execute(query)
        self.session.commit()

    def select(self, **filters):
        query = select(Review).filter_by(**filters)
        result = self.session.execute(query)
        return result.scalars().all()