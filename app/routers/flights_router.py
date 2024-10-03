from fastapi import APIRouter, Depends, HTTPException, Request
from app.services.notify_flight_service import send_flight_info_to_flight_service
from app.models.flight_model import FlightCreate

router = APIRouter()


@router.post("/submit_flight", tags=["flights"])
def submit_flight(flight_data: FlightCreate, request: Request):
    user_id = request.session.get('user_id')
    if not user_id:
        raise HTTPException(status_code=401, detail="User not logged in")

    response = send_flight_info_to_flight_service(user_id, flight_data.dict())

    return {"message": "Flight information sent successfully", "response": response}
