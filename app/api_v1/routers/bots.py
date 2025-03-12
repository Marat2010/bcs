from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()


# Модель для бота
class Bot(BaseModel):
    id: int
    name: str
    description: str = None


# Список для хранения ботов
bots_db = []


@router.post("/bots/", response_model=Bot)
def create_bot(bot: Bot):
    bots_db.append(bot)
    return bot


@router.get("/bots/", response_model=List[Bot])
def read_bots():
    return bots_db

