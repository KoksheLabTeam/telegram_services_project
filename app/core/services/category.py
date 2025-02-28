from app.core.models.category import Category
from app.core.schemas.category import CategoryCreate, CategoryUpdate, CategoryResponse
from app.core.repos.category import CategoryRepo, CategoryCreateException, CategoryNotFoundException
from fastapi import HTTPException


class CategoryService:
    def __init__(self, repository: CategoryRepo) -> None:
        self.repository = repository

    def create(self, data: CategoryCreate) -> CategoryResponse:
        instance = Category(name=data.name)

        try:
            category = self.repository.create(instance)
            return CategoryResponse.from_orm(category)
        except CategoryCreateException as e:
            raise HTTPException(status_code=500, detail=f"Error while creating category: {e}")

    def get_by_id(self, category_id: int) -> CategoryResponse:
        category = self.repository.get_by_id(category_id)
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")
        return CategoryResponse.from_orm(category)

    def update(self, category_id: int, update_data: CategoryUpdate) -> CategoryResponse:
        try:
            category = self.repository.update(category_id, update_data)
            return CategoryResponse.from_orm(category)
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
