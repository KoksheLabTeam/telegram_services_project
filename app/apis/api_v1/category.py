from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.schemas.category import CategoryCreate, CategoryUpdate, CategoryRead
from app.core.services.category import CategoryService
from app.core.repos.category import CategoryRepo
from app.core.database.helper import get_session

router = APIRouter()

@router.post("/categories/", response_model=CategoryRead)
def create_category(category: CategoryCreate, db: Session = Depends(get_session)):
    service = CategoryService(CategoryRepo(db))
    return service.create(category)

@router.get("/categories/{category_id}", response_model=CategoryRead)
def get_category(category_id: int, db: Session = Depends(get_session)):
    service = CategoryService(CategoryRepo(db))
    return service.get_by_id(category_id)

@router.put("/categories/{category_id}", response_model=CategoryRead)
def update_category(category_id: int, category: CategoryUpdate, db: Session = Depends(get_session)):
    service = CategoryService(CategoryRepo(db))
    return service.update(category_id, category)

@router.delete("/categories/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_session)):
    service = CategoryService(CategoryRepo(db))
    service.delete(category_id)
    return {"detail": "Category deleted successfully"}

@router.get("/categories/select/", response_model=list[CategoryRead])
def select_categories(filters: dict = Depends(), db: Session = Depends(get_session)):
    service = CategoryService(CategoryRepo(db))
    return service.select(**filters)