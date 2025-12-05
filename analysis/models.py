from pydantic import BaseModel

class TwinData(BaseModel):
    today_minutes: int
    weekly_minutes: int
    night_minutes: int
    sessions_per_day: int
    gaming_ratio: float
    daily_threshold: int
    night_threshold: int
