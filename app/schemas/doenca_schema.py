from pydantic import BaseModel
from typing import Optional

class Doenca(BaseModel):
    id: Optional[int] = None
    nome: str
    causa: str
    profilaxia: str
    sintomas: str
    tratamento: str
    observacoes: Optional[str]

    class Config:
        from_attributes = True