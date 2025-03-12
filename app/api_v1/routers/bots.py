from fastapi import APIRouter
from typing import List

from app.api_v1.schemas.bots import Bot
from app.db.models import bots_db

router = APIRouter()


@router.post("/bots/", response_model=Bot)
def create_bot(bot: Bot):
    bots_db.append(bot)
    return bot


@router.get("/bots/", response_model=List[Bot])
def read_bots():
    return bots_db

