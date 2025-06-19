from pydantic import BaseModel
from typing import Optional

class Fazenda(BaseModel):
    id: Optional[int] = None
    nome: str
    localizacao: Optional[str]
    responsavel: Optional[str]

    class Config:
        from_attributes = True