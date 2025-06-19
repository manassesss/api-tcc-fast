from pydantic import BaseModel
from typing import Optional
from datetime import date

class OcorrenciaClinica(BaseModel):
    id: Optional[int] = None
    animal_id: int
    doenca_id: int
    data_ocorrencia: date
    observacoes: Optional[str]

    class Config:
        from_attributes = True
