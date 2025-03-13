from fastapi import FastAPI
from app.api_v1 import router as api_v1_router  # Явно указываем, что это весь API v1

app = FastAPI()

app.include_router(api_v1_router, prefix="/api/v1")
