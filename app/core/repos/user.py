from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from app.core.models.user import User

class UserCreateException(Exception):
    """Raise exception when there is an error during user creation."""

class UserNotFoundException(Exception):
    """Raise exception when no user is found."""

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

    def get_by_id(self, user_id: int) -> User:
        query = select(User).where(User.id == user_id)
        result = self.session.execute(query)
        user = result.scalar_one_or_none()
        if not user:
            raise UserNotFoundException(f"User with id '{user_id}' not found")
        return user

    def update(self, user_id: int, update_data: dict) -> User:
        query = (
            update(User)
            .where(User.id == user_id)
            .values(**update_data)
            .returning(User)
        )
        result = self.session.execute(query)
        self.session.commit()
        return result.scalar_one()

    def delete(self, user_id: int) -> None:
        query = delete(User).where(User.id == user_id)
        self.session.execute(query)
        self.session.commit()

    def select(self, **filters):
        query = select(User).filter_by(**filters)
        result = self.session.execute(query)
        return result.scalars().all()