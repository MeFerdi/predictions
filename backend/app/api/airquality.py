from fastapi import APIRouter, Query
from pydantic import BaseModel
from typing import List
from datetime import datetime

router = APIRouter()


class Pollutant(BaseModel):
    name: str
    value: float


class ForecastResponse(BaseModel):
    city: str
    timestamp: str
    aqi: int
    pollutants: List[Pollutant]
    forecast: List[int]
    health_advice: str


@router.get("/", response_model=ForecastResponse)
async def get_airquality(city: str = Query(..., description="City name to query")):
    """
    Mock endpoint that returns a structured air quality response.
    The implementation is intentionally modular — data adapters for TEMPO, PurpleAir, NOAA
    should be added under backend/app/adapters and wired here.
    """
    # Mocked data for local development
    now = datetime.utcnow().isoformat() + "Z"
    pollutants = [
        {"name": "PM2.5", "value": 12.4},
        {"name": "O3", "value": 0.032},
        {"name": "NO2", "value": 0.018},
    ]
    forecast = [45, 50, 60, 70, 85, 90, 110, 120, 100, 80, 65, 55, 50, 48, 46, 44, 42, 40, 38, 35, 33, 30, 28, 25]

    return {
        "city": city,
        "timestamp": now,
        "aqi": 92,
        "pollutants": pollutants,
        "forecast": forecast,
        "health_advice": "Some sensitive groups should reduce prolonged or heavy exertion outdoors.",
    }
