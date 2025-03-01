from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.core.schemas.review import ReviewCreate, ReviewUpdate, ReviewRead
from app.core.services.review import ReviewService
from app.core.repos.review import ReviewRepo
from app.core.database.helper import get_session

router = APIRouter(prefix="/reviews", tags=["reviews"])

def parse_filters(order_id: int = Query(None), author_id: int = Query(None)) -> dict:
    filters = {}
    if order_id:
        filters["order_id"] = order_id
    if author_id:
        filters["author_id"] = author_id
    return filters

@router.post("/", response_model=ReviewRead)
def create_review(review: ReviewCreate, db: Session = Depends(get_session)):
    service = ReviewService(ReviewRepo(db))
    return service.create(review)

@router.get("/{review_id}", response_model=ReviewRead)
def get_review(review_id: int, db: Session = Depends(get_session)):
    service = ReviewService(ReviewRepo(db))
    return service.get_by_id(review_id)

@router.put("/{review_id}", response_model=ReviewRead)
def update_review(review_id: int, review: ReviewUpdate, db: Session = Depends(get_session)):
    service = ReviewService(ReviewRepo(db))
    return service.update(review_id, review)

@router.delete("/{review_id}")
def delete_review(review_id: int, db: Session = Depends(get_session)):
    service = ReviewService(ReviewRepo(db))
    service.delete(review_id)
    return {"detail": "Review deleted successfully"}

@router.get("/select/", response_model=list[ReviewRead])
def select_reviews(filters: dict = Depends(parse_filters), db: Session = Depends(get_session)):
    service = ReviewService(ReviewRepo(db))
    return service.select(**filters)