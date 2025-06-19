from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.medicamento_schema import Medicamento as MedicamentoSchema
from app.models.medicamento import Medicamento as MedicamentoModel
from app.db.dependency import get_db
from typing import List
from app.core.deps import get_current_user        # 👈 novo

router = APIRouter(prefix="/medicamentos", tags=["Medicamentos"])

@router.post("/", response_model=MedicamentoSchema)
def criar_medicamento(medicamento: MedicamentoSchema, db: Session = Depends(get_current_user)):
    db_medicamento = MedicamentoModel(**medicamento.dict(exclude_unset=True))
    db.add(db_medicamento)
    db.commit()
    db.refresh(db_medicamento)
    return db_medicamento

@router.get("/", response_model=List[MedicamentoSchema])
def listar_medicamentos(db: Session = Depends(get_current_user)):
    return db.query(MedicamentoModel).all()