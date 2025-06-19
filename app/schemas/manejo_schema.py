from pydantic import BaseModel
from typing import Optional
from datetime import date

class ManejoReprodutivo(BaseModel):
    id: Optional[int] = None
    rebanho_id: int
    matriz_id: int
    reprodutor_id: int
    data_cobertura: date
    peso_matriz: Optional[float]
    escore_matriz: Optional[int]
    perimetro_escrotal: Optional[float]
    paricao_status: Optional[str]
    data_parto: Optional[date]
    tipo_parto: Optional[str]
    data_desmame: Optional[date]
    observacoes: Optional[str]

    class Config:
        from_attributes = True
