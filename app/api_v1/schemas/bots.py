from pydantic import BaseModel


# Модель для бота
class Bot(BaseModel):
    id: int
    name: str
    description: str = None
    token: str = None
    port: int = None
    active: bool = False

