
from pydantic import BaseModel
from datetime import date
from typing import Optional

class Animal(BaseModel):
    id: Optional[int] = None
    nome: str
    sexo: str
    data_nascimento: Optional[date]
    rebanho_id: Optional[int]
    indice_genetico: float = 0.0
    
    pai_codigo: Optional[str]
    mae_codigo: Optional[str]
    categoria: Optional[str]
    raca: Optional[str]
    finalidade: Optional[str]
    tipo_parto: Optional[str]
    composicao_genetica: Optional[str]

    data_desmame: Optional[date]
    peso: Optional[float]
    ecc: Optional[int]
    conformacao: Optional[int]
    precocidade: Optional[int]
    musculatura: Optional[int]

    altura_garupa: Optional[float]
    altura_paleta: Optional[float]
    altura_cernelha: Optional[float]
    comprimento_corporal: Optional[float]
    perimetro_toracico: Optional[float]

    area_olho_lombo: Optional[float]
    gordura_subcutanea: Optional[float]
    espessura_gordura: Optional[float]
    profundidade_olho_lombo: Optional[float]

    data_medição_verminose: Optional[date]
    opg: Optional[int]

    class Config:
        from_attributes = True
