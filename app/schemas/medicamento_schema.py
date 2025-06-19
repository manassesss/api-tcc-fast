from pydantic import BaseModel
from typing import Optional

class Medicamento(BaseModel):
    id: Optional[int] = None
    nome: str
    descricao: str

    class Config:
        from_attributes = True
