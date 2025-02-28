from fastapi import APIRouter, Depends
from app.core.schemas.user import UserCreate, UserResponse
from app.core.services.user import UserService
from app.core.repos.user import UserRepo
from sqlalchemy.orm import Session
from app.core.database.helper import get_session

router = APIRouter()

@router.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_session)):
    user_service = UserService(UserRepo(db))
    return user_service.create(user)

@router.get("/users/{telegram_id}", response_model=UserResponse)
def get_user(telegram_id: int, db: Session = Depends(get_session)):
    user_service = UserService(UserRepo(db))
    return user_service.get_by_telegram_id(telegram_id)

@router.put("/users/{telegram_id}", response_model=UserResponse)
def update_user(telegram_id: int, user_update: dict, db: Session = Depends(get_session)):
    user_service = UserService(UserRepo(db))
    return user_service.update(telegram_id, user_update)

@router.delete("/users/{telegram_id}")
def delete_user(telegram_id: int, db: Session = Depends(get_session)):
    user_service = UserService(UserRepo(db))
    user_service.delete(telegram_id)
    return {"detail": "User deleted successfully"}
