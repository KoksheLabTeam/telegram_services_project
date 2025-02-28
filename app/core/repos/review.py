from sqlalchemy import select
from sqlalchemy.orm import Session
from app.core.models.review import Review


class ReviewCreateException(Exception):
    """Raise exception when there is an error during review creation"""


class ReviewNotFoundException(Exception):
    """Raise exception when there is no review found"""


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

    def get(self, review_id: int) -> Review:
        query = select(Review).where(Review.id == review_id)
        try:
            review = self.session.execute(query)
            return review.scalar_one_or_none()
        except Exception as e:
            self.session.rollback()
            raise ReviewNotFoundException(str(e))

    def update(self, review_id: int, data: dict) -> Review:
        review = self.get(review_id)
        if not review:
            raise ReviewNotFoundException("Review not found")

        for key, value in data.items():
            setattr(review, key, value)

        try:
            self.session.commit()
            self.session.refresh(review)
            return review
        except Exception as e:
            self.session.rollback()
            raise Exception(f"Error updating review: {str(e)}")

    def delete(self, review_id: int) -> None:
        review = self.get(review_id)
        if not review:
            raise ReviewNotFoundException("Review not found")

        try:
            self.session.delete(review)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise Exception(f"Error deleting review: {str(e)}")

    def filter_by_target(self, target_id: int):
        query = select(Review).where(Review.target_id == target_id)
        return self.session.execute(query).scalars().all()

    def filter_by_author(self, author_id: int):
        query = select(Review).where(Review.author_id == author_id)
        return self.session.execute(query).scalars().all()
