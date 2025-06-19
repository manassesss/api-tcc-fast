from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.parasita_schema import ControleParasitario as ParasitaSchema
from app.models.controle_parasitario import ControleParasitario as ParasitaModel
from app.db.dependency import get_db
from typing import List
from app.core.deps import get_current_user        # 👈 novo

router = APIRouter(prefix="/controles-parasitarios", tags=["Controle Parasitário"])

@router.post("/", response_model=ParasitaSchema)
def criar_controle_parasitario(parasita: ParasitaSchema, db: Session = Depends(get_current_user)):
    db_obj = ParasitaModel(**parasita.dict(exclude_unset=True))
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

@router.get("/", response_model=List[ParasitaSchema])
def listar_controles_parasitarios(db: Session = Depends(get_current_user)):
    return db.query(ParasitaModel).all()
