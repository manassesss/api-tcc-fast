from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.ocorrencia_schema import OcorrenciaClinica as OcorrenciaSchema
from app.models.ocorrencia_clinica import OcorrenciaClinica as OcorrenciaModel
from app.db.dependency import get_db
from typing import List
from app.core.deps import get_current_user        # 👈 novo

router = APIRouter(prefix="/ocorrencias-clinicas", tags=["Ocorrências Clínicas"])

@router.post("/", response_model=OcorrenciaSchema)
def criar_ocorrencia(ocorrencia: OcorrenciaSchema, db: Session = Depends(get_current_user)):
    db_ocorrencia = OcorrenciaModel(**ocorrencia.dict(exclude_unset=True))
    db.add(db_ocorrencia)
    db.commit()
    db.refresh(db_ocorrencia)
    return db_ocorrencia

@router.get("/", response_model=List[OcorrenciaSchema])
def listar_ocorrencias(db: Session = Depends(get_current_user)):
    return db.query(OcorrenciaModel).all()
