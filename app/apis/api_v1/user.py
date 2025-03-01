from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.core.schemas.user import UserCreate, UserUpdate, UserRead
from app.core.services.user import UserService
from app.core.repos.user import UserRepo
from app.core.database.helper import get_session

router = APIRouter(prefix="/users", tags=["users"])

def parse_filters(telegram_id: int = Query(None), name: str = Query(None)) -> dict:
    filters = {}
    if telegram_id:
        filters["telegram_id"] = telegram_id
    if name:
        filters["name"] = name
    return filters

@router.post("/", response_model=UserRead)
def create_user(user: UserCreate, db: Session = Depends(get_session)):
    user_service = UserService(UserRepo(db))
    return user_service.create(user)

@router.get("/{telegram_id}", response_model=UserRead)
def get_user(telegram_id: int, db: Session = Depends(get_session)):
    user_service = UserService(UserRepo(db))
    return user_service.get_by_telegram_id(telegram_id)

@router.put("/{telegram_id}", response_model=UserRead)
def update_user(telegram_id: int, user_update: UserUpdate, db: Session = Depends(get_session)):
    user_service = UserService(UserRepo(db))
    return user_service.update(telegram_id, user_update)

@router.delete("/{telegram_id}")
def delete_user(telegram_id: int, db: Session = Depends(get_session)):
    user_service = UserService(UserRepo(db))
    user_service.delete(telegram_id)
    return {"detail": "User deleted successfully"}

@router.get("/select/", response_model=list[UserRead])
def select_users(filters: dict = Depends(parse_filters), db: Session = Depends(get_session)):
    user_service = UserService(UserRepo(db))
    return user_service.select(**filters)