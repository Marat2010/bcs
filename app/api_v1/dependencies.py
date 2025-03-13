from typing import List
from app.db.models import bots_db


# Зависимость для получения базы данных ботов
def get_bots_db() -> List:
    return bots_db

