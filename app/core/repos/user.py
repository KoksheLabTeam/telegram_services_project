from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session

from app.core.models.user import User
from app.core.schemas.user import UserResponse

class UserCreateException(Exception):
    """Raise exception when there is an error during user creation"""

class UserNotFoundException(Exception):
    """Raise exception when there is no user found"""

class UserRepo:
    def __init__(self, session: Session) -> None:
        self.session = session

    def create(self, instance: User) -> UserResponse:
        self.session.add(instance)
        try:
            self.session.commit()
            self.session.refresh(instance)
            return UserResponse.from_orm(instance)
        except Exception as e:
            self.session.rollback()
            raise UserCreateException(str(e))

    def get(self, username: str) -> UserResponse:
        query = select(User).where(User.username == username)
        try:
            user = self.session.execute(query).scalar_one_or_none()
            if user is None:
                raise UserNotFoundException("User not found")
            return UserResponse.from_orm(user)
        except Exception as e:
            self.session.rollback()
            raise UserNotFoundException(str(e))

    def update(self, user_id: int, update_data: dict) -> UserResponse:
        query = update(User).where(User.id == user_id).values(**update_data).returning(User)
        try:
            result = self.session.execute(query)
            self.session.commit()
            user = result.scalar_one()
            return UserResponse.from_orm(user)
        except Exception as e:
            self.session.rollback()
            raise UserCreateException(str(e))

    def delete(self, user_id: int) -> None:
        query = delete(User).where(User.id == user_id)
        try:
            self.session.execute(query)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise UserCreateException(str(e))

    def select_users(self, **filters):
        query = select(User).where(*[getattr(User, key) == value for key, value in filters.items()])
        try:
            result = self.session.execute(query)
            return [UserResponse.from_orm(user) for user in result.scalars().all()]
        except Exception as e:
            self.session.rollback()
            raise UserCreateException(str(e))
