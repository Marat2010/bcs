from typing import Optional
from pydantic import BaseModel, Field


# Модель для бота
class Bot(BaseModel):
    id: int
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = None
    token: Optional[str] = None
    port: Optional[int] = None
    active: bool = False

