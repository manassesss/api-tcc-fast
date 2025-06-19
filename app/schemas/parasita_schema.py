from pydantic import BaseModel
from typing import Optional
from datetime import date

class ControleParasitario(BaseModel):
    id: Optional[int] = None
    animal_id: int
    medicamento_id: int
    data_vermifugacao: date
    opg_pre: Optional[int]
    opg_pos: Optional[int]
    escore_corporal: Optional[int]
    famacha: Optional[int]
    observacoes: Optional[str]

    class Config:
        from_attributes = True
