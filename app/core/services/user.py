from app.core.models.user import User
from app.core.schemas.user import UserCreate
from app.core.repos.user import UserRepo, UserCreateExeption
from fastapi import HTTPException

# API -> Service -> Repo хранить бизнес логику, калькуляцию к примеру (ответы тестов пришли, и внутри сервиса,
# и на сколько ответили правильно и неправильно все тут, и конечный результат тоже будем писать тут

# user depency -> get_user_service -> service,
# get_curent_user
# get_admin_user для прав админа

class UserService:
    def __init__(self, repository: UserRepo) -> None:
        self.repository = repository

    def create(self, data: UserCreate) -> User:
        instance = User(
            username = data.username,
            password = data.password,
            first_name = data.first_name,
            last_name = data.last_name,
            middle_name = data.middle_name if not data.middle_name else None, # если не пришел, не будет записывать
            is_active = data.is_active,
            is_staff= data.is_staff,
            is_superuser = data.is_superuser,
        )

        try:
            user = self.repository.create(instance)
            return user
        except UserCreateExeption as e:
            raise HTTPException(status_code=500, detail=f"Error while creating user: {e}"
            )


