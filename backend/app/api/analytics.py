from fastapi import APIRouter
from backend.app.models.responses import AnalyticsResponse

router = APIRouter()

@router.get("/analytics", response_model=AnalyticsResponse)
async def get_dashboard_analytics():
    return {
        "total_translations": 1284,
        "total_words_translated": 48290,
        "average_response_time_ms": 142.5,
        "average_confidence": 0.94,
        "top_language_pairs": [
            {"pair": "EN ➔ HI", "count": 512, "percentage": 39.8},
            {"pair": "EN ➔ ES", "count": 294, "percentage": 22.8},
            {"pair": "EN ➔ FR", "count": 180, "percentage": 14.0},
            {"pair": "TE ➔ EN", "count": 145, "percentage": 11.2},
            {"pair": "ZH ➔ EN", "count": 153, "percentage": 11.9}
        ],
        "daily_stats": [
            {"date": "Mon", "words": 6200},
            {"date": "Tue", "words": 7400},
            {"date": "Wed", "words": 8900},
            {"date": "Thu", "words": 9100},
            {"date": "Fri", "words": 10500},
            {"date": "Sat", "words": 4200},
            {"date": "Sun", "words": 1990}
        ]
    }
