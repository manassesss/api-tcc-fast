from pydantic import BaseModel
from typing import Optional

class Raca(BaseModel):
    id: Optional[int] = None
    nome: str
    origem: Optional[str]
    aspectos_gerais: Optional[str]

    class Config:
        from_attributes = True