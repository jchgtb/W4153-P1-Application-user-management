import requests
from fastapi import HTTPException

def send_flight_info_to_flight_service(user_id: int, flight_data: dict):
    url = "http://127.0.0.1:8000/flights"

    data = {
        "user_id": user_id,
        "flight_number": flight_data["flight_number"],
        "flight_date": flight_data["flight_date"].isoformat(),
        "flight_time": str(flight_data["flight_time"]),
        "departure_location": flight_data["departure_location"]
    }

    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Failed to send flight info: {str(e)}")
