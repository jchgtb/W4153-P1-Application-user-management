from fastapi import APIRouter, Request, HTTPException, Depends
from sqlalchemy.orm import Session
from app.utils.dependencies import get_db
from app.services.notify_matching_service import send_user_id_to_matching_service

router = APIRouter()


@router.post("/match_user", tags=["matching"])
def match_user(request: Request, db: Session = Depends(get_db)):
    user_id = request.session.get('user_id')
    if not user_id:
        raise HTTPException(status_code=401, detail="User not logged in")

    response = send_user_id_to_matching_service(user_id)

    return {"message": "Matching request sent", "response": response}
