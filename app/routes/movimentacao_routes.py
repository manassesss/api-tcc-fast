from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.movimentacao_schema import MovimentacaoAnimal as MovimentacaoSchema
from app.models.movimentacao_animal import MovimentacaoAnimal as MovimentacaoModel
from app.db.dependency import get_db
from typing import List
from app.core.deps import get_current_user        # 👈 novo

router = APIRouter(prefix="/movimentacoes", tags=["Movimentação Animal"])

@router.post("/", response_model=MovimentacaoSchema)
def criar_movimentacao(movimentacao: MovimentacaoSchema, db: Session = Depends(get_current_user)):
    db_mov = MovimentacaoModel(**movimentacao.dict(exclude_unset=True))
    db.add(db_mov)
    db.commit()
    db.refresh(db_mov)
    return db_mov

@router.get("/", response_model=List[MovimentacaoSchema])
def listar_movimentacoes(db: Session = Depends(get_current_user)):
    return db.query(MovimentacaoModel).all()
