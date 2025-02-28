from fastapi import APIRouter, Depends
from app.core.schemas.category import CategoryCreate, CategoryUpdate, CategoryResponse
from app.core.services.category import CategoryService
from app.core.repos.category import CategoryRepo
from sqlalchemy.orm import Session
from app.core.database.helper import get_session

router = APIRouter()

@router.post("/categories/", response_model=CategoryResponse)
def create_category(category: CategoryCreate, db: Session = Depends(get_session)):
    category_service = CategoryService(CategoryRepo(db))
    return category_service.create(category)

@router.get("/categories/{category_id}", response_model=CategoryResponse)
def get_category(category_id: int, db: Session = Depends(get_session)):
    category_service = CategoryService(CategoryRepo(db))
    return category_service.get_by_id(category_id)

@router.put("/categories/{category_id}", response_model=CategoryResponse)
def update_category(category_id: int, category: CategoryUpdate, db: Session = Depends(get_session)):
    category_service = CategoryService(CategoryRepo(db))
    return category_service.update(category_id, category)

@router.delete("/categories/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_session)):
    category_service = CategoryService(CategoryRepo(db))
    category_service.delete(category_id)
    return {"detail": "Category deleted successfully"}
