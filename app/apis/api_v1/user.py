from fastapi import APIRouter, Depends
from typing import Annotated
from app.core.services.user import UserService
from app.apis.depends.user import get_user_service
from app.core.schemas.user import UserCreate

router = APIRouter(prefix="/user344334", tags=["User"])

@router.post("/")
def user_create(
    data: UserCreate,
    service: Annotated[UserService, Depends(get_user_service)],
):
    new_user = service.create(data)
    return new_user

