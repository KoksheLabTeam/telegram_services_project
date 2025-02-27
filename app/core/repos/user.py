from sqlalchemy.orm import Session
from app.core.models.user import User
from app.core.schemas.user import UserCreate, UserUpdate


class UserCreateException(Exception):
    """Выбрасывается при ошибке создания пользователя"""

class UserRepo:
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_by_id(self, user_id: int) -> User | None:
        return self.session.query(User).filter(User.id == user_id).first()

    def get_by_username(self, username: str) -> User | None:
        return self.session.query(User).filter(User.username == username).first()

    def create(self, user_data: UserCreate) -> User:
        instance = User(**user_data.model_dump())
        self.session.add(instance)
        try:
            self.session.commit()
            self.session.refresh(instance)
            return instance
        except Exception as e:
            self.session.rollback()
            raise UserCreateException(str(e))

    def update(self, user: User, user_data: UserUpdate) -> User:
        for key, value in user_data.model_dump(exclude_unset=True).items():
            setattr(user, key, value)
        try:
            self.session.commit()
            self.session.refresh(user)
            return user
        except Exception as e:
            self.session.rollback()
            raise Exception(f"Ошибка обновления пользователя: {str(e)}")

    def delete(self, user: User) -> None:
        self.session.delete(user)
        try:
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise Exception(f"Ошибка удаления пользователя: {str(e)}")
