"""
Mock TEMPO adapter interface.
Real implementation should handle authentication, pagination and rate limits and return structured data.
"""
from typing import Dict, Any


def fetch_tempo_observations(bbox: Dict[str, float]) -> Dict[str, Any]:
    # This is a stub function — replace with real API calls to NASA TEMPO endpoints
    return {
        "no2": 0.02,
        "o3": 0.03,
        "aerosol_index": 0.5,
        "bbox": bbox,
    }
