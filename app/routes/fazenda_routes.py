from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.fazenda_schema import Fazenda as FazendaSchema
from app.models.fazenda import Fazenda as FazendaModel
from app.db.dependency import get_db
from typing import List
from app.core.deps import get_current_user        # 👈 novo

router = APIRouter(prefix="/fazendas", tags=["Fazendas"])

@router.post("/", response_model=FazendaSchema)
def criar_fazenda(fazenda: FazendaSchema, db: Session = Depends(get_current_user)):
    db_fazenda = FazendaModel(**fazenda.dict(exclude_unset=True))
    db.add(db_fazenda)
    db.commit()
    db.refresh(db_fazenda)
    return db_fazenda

@router.get("/", response_model=List[FazendaSchema])
def listar_fazendas(db: Session = Depends(get_current_user)):
    return db.query(FazendaModel).all()