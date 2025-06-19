from pydantic import BaseModel
from typing import Optional

class Funcionario(BaseModel):
    id: Optional[int] = None
    nome: str
    email: Optional[str]
    cpf: str
    endereco: str
    municipio: str
    estado: Optional[str]
    telefone: str
    fazenda_id: int  # obrigatório

    class Config:
        from_attributes = True
