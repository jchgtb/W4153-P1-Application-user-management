from fastapi import APIRouter, Request, Form, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.users_service import UserService
from app.utils.dependencies import get_db
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/login", tags=["auth"])
def login(request: Request, username: str = Form(...), db: Session = Depends(get_db)):
    user_service = UserService(db)
    user = user_service.get_user_by_username(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    request.session['user_id'] = user.user_id
    return JSONResponse(content={"message": "User logged in successfully", "user_id": user.user_id})
