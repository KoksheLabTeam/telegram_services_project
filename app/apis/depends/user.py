from app.core.services.user import UserService
from fastapi import Depends
from typing import Annotated
from sqlalchemy.orm import Session
from app.core.database.helper import get_session
from app.core.repos.user import UserRepo

# user service dependency
def get_user_service(
        session: Annotated[Session, Depends(get_session)],
) -> UserService:
    user_repo = UserRepo(session)
    user_service = UserService(user_repo)
    return user_service