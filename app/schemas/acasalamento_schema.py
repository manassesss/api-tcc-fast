from pydantic import BaseModel
from typing import Optional
from datetime import date

class Acasalamento(BaseModel):
    id: Optional[int] = None
    matriz_id: int
    reprodutor_id: int
    data_acasalamento: date
    tipo: str
    indice_genetico_progênie: Optional[float]
    endogamia_prevista: Optional[float]
    observacoes: Optional[str]

    class Config:
        from_attributes = True
