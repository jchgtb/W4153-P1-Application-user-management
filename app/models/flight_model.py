from pydantic import BaseModel
from datetime import date, time

class FlightCreate(BaseModel):
    flight_number: str
    flight_date: date
    flight_time: time
    departure_location: str

    class Config:
        schema_extra = {
            "example": {
                "flight_number": "UA1234",
                "flight_date": "2024-10-02",
                "flight_time": "15:30:00",
                "departure_location": "JFK"
            }
        }
