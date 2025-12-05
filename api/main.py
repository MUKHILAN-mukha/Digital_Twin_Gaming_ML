from fastapi import FastAPI
from api.ml_routes import router as ml_router

app = FastAPI()

# Register ML analyzer routes
app.include_router(ml_router)
