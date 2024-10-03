from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.users_service import UserService
from app.utils.dependencies import get_db
from app.models.user_model import UserCreate

router = APIRouter()

@router.post("/users", tags=["users"])
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    user_service = UserService(db)
    return user_service.create_user(
        username=user_data.username,
        email=user_data.email,
        phone_number=user_data.phone_number
    )
