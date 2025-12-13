from api.ml_engine import analyze_with_ml
from fastapi import APIRouter

router = APIRouter()

@router.post("/analyze-ml")
def analyze_ml(payload: dict):
    twin = payload["digital_twin"]        # extracted from Member 2 backend
    result = analyze_with_ml(twin)
    return result
