from pydantic import BaseModel
from typing import Optional
from datetime import date

class Vacinacao(BaseModel):
    id: Optional[int] = None
    animal_id: int
    medicamento_id: int
    data_vacinacao: date
    observacoes: Optional[str]

    class Config:
        from_attributes = True
