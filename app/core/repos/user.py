from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session

from app.core.models.user import User


class UserCreateException(Exception):
    """Raise exception when there is an error during user creation"""


class UserNotFoundException(Exception):
    """Raise exception when there is no user found"""


class UserRepo:
    def __init__(self, session: Session) -> None:
        self.session = session

    def create(self, instance: User) -> User:
        self.session.add(instance)
        try:
            self.session.commit()
            self.session.refresh(instance)
            return instance

        except Exception as e:
            self.session.rollback()
            raise UserCreateException(str(e))

    def get(self, username: str) -> User:
        query = select(User).where(User.username == username)

        try:
            user = self.session.execute(query)
            return user.scalar_one_or_none()

        except Exception as e:
            self.session.rollback()
            raise UserNotFoundException(str(e))

    def update(self, user_id: int, update_data: dict) -> User:
        query = update(User).where(User.id == user_id).values(**update_data).returning(User)
        try:
            result = self.session.execute(query)
            self.session.commit()
            return result.scalar_one()
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

    def filter_users(self, **filters):
        query = select(User).filter_by(**filters)
        try:
            result = self.session.execute(query)
            return result.scalars().all()
        except Exception as e:
            self.session.rollback()
            raise UserCreateException(str(e))
