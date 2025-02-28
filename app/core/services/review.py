from fastapi import HTTPException
from app.core.models.review import Review
from app.core.schemas.review import ReviewCreate, ReviewUpdate, ReviewRead
from app.core.repos.review import ReviewRepo, ReviewCreateException, ReviewNotFoundException

class ReviewService:
    def __init__(self, repository: ReviewRepo) -> None:
        self.repository = repository

    def create(self, data: ReviewCreate) -> ReviewRead:
        instance = Review(
            order_id=data.order_id,
            author_id=data.author_id,
            target_id=data.target_id,
            rating=data.rating,
            comment=data.comment,
        )
        try:
            review = self.repository.create(instance)
            return ReviewRead.from_orm(review)
        except ReviewCreateException as e:
            raise HTTPException(status_code=500, detail=f"Error while creating review: {e}")

    def get_by_id(self, review_id: int) -> ReviewRead:
        try:
            review = self.repository.get_by_id(review_id)
            if not review:
                raise HTTPException(status_code=404, detail="Review not found")
            return ReviewRead.from_orm(review)
        except ReviewNotFoundException:
            raise HTTPException(status_code=404, detail="Review not found")

    def update(self, review_id: int, update_data: ReviewUpdate) -> ReviewRead:
        try:
            review = self.repository.update(review_id, update_data.dict(exclude_unset=True))
            return ReviewRead.from_orm(review)
        except ReviewNotFoundException:
            raise HTTPException(status_code=404, detail="Review not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error while updating review: {e}")

    def delete(self, review_id: int) -> None:
        try:
            self.repository.delete(review_id)
        except ReviewNotFoundException:
            raise HTTPException(status_code=404, detail="Review not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error while deleting review: {e}")

    def select(self, **filters):
        reviews = self.repository.select(**filters)
        if not reviews:
            raise HTTPException(status_code=404, detail="No reviews found")
        return [ReviewRead.from_orm(review) for review in reviews]