# api/main.py

from fastapi import FastAPI
from api.ml_routes import router as ml_router

app = FastAPI(
    title="Gaming Behavior ML Engine (Member 3)",
)

app.include_router(ml_router)
