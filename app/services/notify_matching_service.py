import requests
from fastapi import HTTPException

def send_user_id_to_matching_service(user_id: int):
    url = "http://127.0.0.1:8010/match"

    data = {"user_id": user_id}

    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Failed to send match request: {str(e)}")
