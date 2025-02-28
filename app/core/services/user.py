from fastapi import HTTPException
from app.core.models.user import User
from app.core.repos.user import UserRepo, UserCreateException
from app.core.schemas.user import UserCreate, UserResponse


class UserService:
    def __init__(self, repository: UserRepo) -> None:
        self.repository = repository

    def create(self, data: UserCreate) -> UserResponse:
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
            return UserResponse.from_orm(user)
        except UserCreateException as e:
            raise HTTPException(status_code=500, detail=f"Error while creating user: {e}")

    def get_by_telegram_id(self, telegram_id: int) -> UserResponse:
        user = self.repository.get_by_telegram_id(telegram_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return UserResponse.from_orm(user)

    def update(self, telegram_id: int, update_data: dict) -> UserResponse:
        try:
            user = self.repository.update(telegram_id, update_data)
            return UserResponse.from_orm(user)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error while updating user: {e}")

    def delete(self, telegram_id: int) -> None:
        try:
            self.repository.delete(telegram_id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error while deleting user: {e}")
