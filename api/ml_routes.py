from fastapi import APIRouter, HTTPException
from api.ml_engine import analyze_with_ml
import requests
import os

router = APIRouter()

# Member 2’s backend URL
BASE_URL = os.getenv("MEMBER2_URL", "http://localhost:8000")
API_KEY = os.getenv("MEMBER2_API_KEY")   # needed because he uses middleware

@router.get("/analyze-ml/{user_id}")
def analyze_ml(user_id: str):

    # 1. Fetch twin data from Member 2 backend
    try:
        resp = requests.get(
            f"{BASE_URL}/digital-twin/{user_id}",
            headers={"X-API-KEY": API_KEY}
        )
        resp.raise_for_status()
        twin = resp.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch twin: {e}")

    # 2. Convert Member 2's structure into your ML model’s expected structure
    twin_data = {
        "today_minutes": twin["aggregates"]["today_minutes"],
        "weekly_minutes": twin["aggregates"]["weekly_minutes"],
        "night_minutes": twin["aggregates"]["night_minutes"],
        "sessions_per_day": twin["aggregates"]["sessions_per_day"],
        "gaming_ratio": twin["aggregates"]["today_minutes"] / max(twin["aggregates"]["weekly_minutes"], 1),
        "daily_threshold": twin["thresholds"]["daily"],
        "night_threshold": twin["thresholds"]["night"]
    }

    # 3. Send to your ML + rules engine
    result = analyze_with_ml(twin_data)

    # 4. Return to frontend
    return {
        "user_id": user_id,
        "original_data": twin,
        "analysis_results": result
    }
