from fastapi import HTTPException
from app.core.models.user import User
from app.core.schemas.user import UserCreate, UserUpdate, UserRead
from app.core.repos.user import UserRepo, UserCreateException, UserNotFoundException
from app.core.models.category import Category

class UserService:
    def __init__(self, repository: UserRepo) -> None:
        self.repository = repository

    def create(self, data: UserCreate) -> UserRead:
        instance = User(
            telegram_id=data.telegram_id,
            name=data.name,
            username=data.username,
            is_customer=data.is_customer,
            is_executor=data.is_executor,
            is_admin=data.is_admin,
            city_id=data.city_id,
            rating=data.rating,
            completed_orders=data.completed_orders,
        )
        try:
            user = self.repository.create(instance)
            return UserRead.from_orm(user)
        except UserCreateException as e:
            raise HTTPException(status_code=500, detail=f"Error while creating user: {e}")

    def get_by_telegram_id(self, telegram_id: int) -> UserRead:
        try:
            user = self.repository.get_by_telegram_id(telegram_id)
            if not user:
                raise HTTPException(status_code=404, detail="User not found")
            return UserRead.from_orm(user)
        except UserNotFoundException:
            raise HTTPException(status_code=404, detail="User not found")

    # app/core/services/user.py
    def update(self, telegram_id: int, update_data: UserUpdate) -> UserRead:
        try:
            update_dict = update_data.model_dump(exclude_unset=True, exclude={"categories"})
            user = self.repository.update(telegram_id, update_dict)
            if "categories" in update_data.model_dump(exclude_unset=True):
                user.categories = [self.repository.session.get(Category, cat_id) for cat_id in update_data.categories]
                self.repository.session.commit()
            return UserRead.from_orm(user)
        except UserNotFoundException:
            raise HTTPException(status_code=404, detail="User not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error while updating user: {e}")

    def delete(self, telegram_id: int) -> None:
        try:
            self.repository.delete(telegram_id)
        except UserNotFoundException:
            raise HTTPException(status_code=404, detail="User not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error while deleting user: {e}")

    def select(self, **filters):
        users = self.repository.select(**filters)
        if not users:
            raise HTTPException(status_code=404, detail="No users found")
        return [UserRead.from_orm(user) for user in users]