from fastapi import APIRouter, Depends
from typing import List

from app.api_v1.schemas.bots import Bot
from app.api_v1.dependencies import get_bots_db  # Импортируем зависимость

router = APIRouter()


@router.post("/", response_model=Bot)
def create_bot(bot: Bot, bots_db: List[Bot] = Depends(get_bots_db)):
    bots_db.append(bot)
    return bot


@router.get("/", response_model=List[Bot])
def read_bots(bots_db: List[Bot] = Depends(get_bots_db)):
    return bots_db

# ===========================

