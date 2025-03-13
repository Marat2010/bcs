from fastapi import APIRouter
from .routers.bots import router as bots_router

router = APIRouter()
router.include_router(bots_router, prefix="/bots", tags=["Боты"])

# =============================
# router.include_router(users_router, prefix="/users")
