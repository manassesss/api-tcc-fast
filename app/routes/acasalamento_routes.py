from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.acasalamento_schema import Acasalamento as AcasalamentoSchema
from app.models.acasalamento import Acasalamento as AcasalamentoModel
from app.db.dependency import get_db
from typing import List
from app.core.deps import get_current_user        # 👈 novo

router = APIRouter(prefix="/acasalamentos", tags=["Acasalamentos"])

@router.post("/", response_model=AcasalamentoSchema)
def criar_acasalamento(acasalamento: AcasalamentoSchema, db: Session = Depends(get_current_user)):
    db_acasalamento = AcasalamentoModel(**acasalamento.dict(exclude_unset=True))
    db.add(db_acasalamento)
    db.commit()
    db.refresh(db_acasalamento)
    return db_acasalamento

@router.get("/", response_model=List[AcasalamentoSchema])
def listar_acasalamentos(db: Session = Depends(get_current_user)):
    return db.query(AcasalamentoModel).all()
