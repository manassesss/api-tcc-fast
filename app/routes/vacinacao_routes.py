from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.vacinacao_schema import Vacinacao as VacinacaoSchema
from app.models.vacinacao import Vacinacao as VacinacaoModel
from app.db.dependency import get_db
from typing import List
from app.core.deps import get_current_user        # 👈 novo

router = APIRouter(prefix="/vacinacoes", tags=["Vacinação"])

@router.post("/", response_model=VacinacaoSchema)
def criar_vacinacao(vacinacao: VacinacaoSchema, db: Session = Depends(get_current_user)):
    db_obj = VacinacaoModel(**vacinacao.dict(exclude_unset=True))
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

@router.get("/", response_model=List[VacinacaoSchema])
def listar_vacinacoes(db: Session = Depends(get_current_user)):
    return db.query(VacinacaoModel).all()
