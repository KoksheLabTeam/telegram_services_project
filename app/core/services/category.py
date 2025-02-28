# app/core/services/category.py
from fastapi import HTTPException
from app.core.models.category import Category
from app.core.schemas.category import CategoryCreate, CategoryUpdate, CategoryRead
from app.core.repos.category import CategoryRepo, CategoryCreateException, CategoryNotFoundException

class CategoryService:
    def __init__(self, repository: CategoryRepo) -> None:
        self.repository = repository

    def create(self, data: CategoryCreate) -> CategoryRead:
        instance = Category(name=data.name)
        try:
            category = self.repository.create(instance)
            return CategoryRead.from_orm(category)
        except CategoryCreateException as e:
            raise HTTPException(status_code=500, detail=f"Error while creating category: {e}")

    def get_by_id(self, category_id: int) -> CategoryRead:
        try:
            category = self.repository.get_by_id(category_id)
            if not category:
                raise HTTPException(status_code=404, detail="Category not found")
            return CategoryRead.from_orm(category)
        except CategoryNotFoundException:
            raise HTTPException(status_code=404, detail="Category not found")

    def update(self, category_id: int, update_data: CategoryUpdate) -> CategoryRead:
        try:
            category = self.repository.update(category_id, update_data.dict(exclude_unset=True))
            return CategoryRead.from_orm(category)
        except CategoryNotFoundException:
            raise HTTPException(status_code=404, detail="Category not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error while updating category: {e}")

    def delete(self, category_id: int) -> None:
        try:
            self.repository.delete(category_id)
        except CategoryNotFoundException:
            raise HTTPException(status_code=404, detail="Category not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error while deleting category: {e}")

    def select(self, **filters):
        categories = self.repository.select(**filters)
        if not categories:
            raise HTTPException(status_code=404, detail="No categories found")
        return [CategoryRead.from_orm(category) for category in categories]