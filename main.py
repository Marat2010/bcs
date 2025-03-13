from fastapi import FastAPI
# from app.api_v1.routers.bots import router as bots_router
from app.api_v1 import router as bots_router

app = FastAPI()

app.include_router(bots_router, prefix="/api/v1")

