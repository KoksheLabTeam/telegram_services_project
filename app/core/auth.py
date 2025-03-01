from fastapi import Depends, HTTPException, Header
from sqlalchemy.orm import Session
from app.core.models.user import User
from app.core.repos.user import UserRepo
from app.core.database.helper import get_session

def get_current_user(telegram_id: str = Header(...), db: Session = Depends(get_session)) -> User:
    """
    Получает текущего пользователя по telegram_id из заголовка запроса.
    """
    try:
        user = UserRepo(db).get_by_telegram_id(int(telegram_id))
        if not user:
            raise HTTPException(status_code=401, detail="User not authenticated")
        return user
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid telegram_id format")

def require_admin(current_user: User = Depends(get_current_user)) -> User:
    """
    Проверяет, является ли текущий пользователь администратором.
    """
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Admin access required")
    return current_user