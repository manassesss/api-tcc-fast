from pydantic import BaseModel
from typing import Optional
from datetime import date

class MovimentacaoAnimal(BaseModel):
    id: Optional[int] = None
    animal_id: int
    peso: Optional[float]
    motivo_saida: str
    data_movimentacao: date

    class Config:
        from_attributes = True
