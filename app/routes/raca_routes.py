from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.raca_schema import Raca as RacaSchema
from app.models.raca import Raca as RacaModel
from app.db.dependency import get_db
from typing import List
from app.core.deps import get_current_user        # 👈 novo

router = APIRouter(prefix="/racas", tags=["Raças"])

@router.post("/", response_model=RacaSchema)
def criar_raca(raca: RacaSchema, db: Session = Depends(get_current_user)):
    db_raca = RacaModel(**raca.dict(exclude_unset=True))
    db.add(db_raca)
    db.commit()
    db.refresh(db_raca)
    return db_raca

@router.get("/", response_model=List[RacaSchema])
def listar_racas(db: Session = Depends(get_current_user)):
    return db.query(RacaModel).all()
