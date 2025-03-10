from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from app.core.models.category import Category

class CategoryCreateException(Exception):
    """Raise exception when there is an error during category creation."""

class CategoryNotFoundException(Exception):
    """Raise exception when no category is found."""

class CategoryRepo:
    def __init__(self, session: Session) -> None:
        self.session = session

    def create(self, instance: Category) -> Category:
        self.session.add(instance)
        try:
            self.session.commit()
            self.session.refresh(instance)
            return instance
        except Exception as e:
            self.session.rollback()
            raise CategoryCreateException(str(e))

    def get_by_id(self, category_id: int) -> Category:
        query = select(Category).where(Category.id == category_id)
        result = self.session.execute(query)
        category = result.scalar_one_or_none()
        if not category:
            raise CategoryNotFoundException(f"Category with id '{category_id}' not found")
        return category

    def update(self, category_id: int, update_data: dict) -> Category:
        query = (
            update(Category)
            .where(Category.id == category_id)
            .values(**update_data)
            .returning(Category)
        )
        result = self.session.execute(query)
        self.session.commit()
        return result.scalar_one()

    def delete(self, category_id: int) -> None:
        query = delete(Category).where(Category.id == category_id)
        self.session.execute(query)
        self.session.commit()

    def select(self, **filters):
        query = select(Category).filter_by(**filters)
        result = self.session.execute(query)
        return result.scalars().all()