
from pydantic import BaseModel
from typing import Optional

class Rebanho(BaseModel):
    id: Optional[int] = None
    nome: str
    descricao: Optional[str]
    fazenda: Optional[str]

    class Config:
        from_attributes = True
