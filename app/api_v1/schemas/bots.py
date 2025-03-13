from pydantic import BaseModel, Field


# Модель для бота
class Bot(BaseModel):
    id: int
    name: str = Field(..., min_length=1, max_length=100)
    description: str = None
    token: str = None
    port: int = None
    active: bool = False

