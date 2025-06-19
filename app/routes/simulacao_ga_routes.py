from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Optional
from app.db.dependency import get_db
from app.services.genetico import executar_ga
from app.core.deps import get_current_user        # 👈 novo

router = APIRouter(prefix="/simular-acasalamentos/ga", tags=["Simulação GA"])

@router.post("/")
def simular_ga(
    rebanho_id: Optional[int] = None,
    peso_endogamia: float = 2.0,
    geracoes: int = 50,
    populacao: int = 30,
    top: int = 10,
    db: Session = Depends(get_current_user)
):
    """
    Retorna as TOP combinações obtidas por Algoritmo Genético.
    """
    return executar_ga(
        db=db,
        rebanho_id=rebanho_id,
        peso_endogamia=peso_endogamia,
        geracoes=geracoes,
        pop_size=populacao,
        top=top
    )
