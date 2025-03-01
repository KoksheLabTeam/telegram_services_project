from fastapi import APIRouter, Depends, Query, Header, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated
from app.core.schemas.user import UserCreate, UserUpdate, UserRead
from app.core.services.user import UserService
from app.core.repos.user import UserRepo
from app.core.database.helper import get_session
from app.core.models.user import User

router = APIRouter(prefix="/users", tags=["users"])

# Зависимость для получения UserService
def get_user_service(session: Annotated[Session, Depends(get_session)]) -> UserService:
    user_repo = UserRepo(session)
    user_service = UserService(user_repo)
    return user_service

# Получение текущего пользователя по telegram_id из заголовка
def get_current_user(
    telegram_id: Annotated[str, Header()],
    user_service: Annotated[UserService, Depends(get_user_service)]
) -> User:
    try:
        user = user_service.get_by_telegram_id(int(telegram_id))
        if not user:
            raise HTTPException(status_code=401, detail="User not authenticated")
        return user
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid telegram_id format")

# Проверка, что пользователь — администратор
def require_admin(current_user: Annotated[User, Depends(get_current_user)]) -> User:
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Admin access required")
    return current_user

# Фильтрация пользователей
def parse_filters(telegram_id: int = Query(None), name: str = Query(None)) -> dict:
    filters = {}
    if telegram_id:
        filters["telegram_id"] = telegram_id
    if name:
        filters["name"] = name
    return filters

@router.post("/", response_model=UserRead)
def create_user(
    user: UserCreate,
    user_service: Annotated[UserService, Depends(get_user_service)]
):
    return user_service.create(user)

@router.get("/{telegram_id}", response_model=UserRead)
def get_user(
    telegram_id: int,
    user_service: Annotated[UserService, Depends(get_user_service)]
):
    return user_service.get_by_telegram_id(telegram_id)

@router.put("/{telegram_id}", response_model=UserRead)
def update_user(
    telegram_id: int,
    user_update: UserUpdate,
    user_service: Annotated[UserService, Depends(get_user_service)]
):
    return user_service.update(telegram_id, user_update)

@router.delete("/{telegram_id}")
def delete_user(
    telegram_id: int,
    user_service: Annotated[UserService, Depends(get_user_service)]
):
    user_service.delete(telegram_id)
    return {"detail": "User deleted successfully"}

@router.get("/select/", response_model=list[UserRead])
def select_users(
    filters: Annotated[dict, Depends(parse_filters)],
    user_service: Annotated[UserService, Depends(get_user_service)]
):
    return user_service.select(**filters)