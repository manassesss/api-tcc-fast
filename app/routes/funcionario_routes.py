from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.funcionario_schema import Funcionario as FuncionarioSchema
from app.models.funcionario import Funcionario as FuncionarioModel
from app.db.dependency import get_db
from typing import List
from app.core.deps import get_current_user        # 👈 novo

router = APIRouter(prefix="/funcionarios", tags=["Funcionários"])

@router.post("/", response_model=FuncionarioSchema)
def criar_funcionario(funcionario: FuncionarioSchema, db: Session = Depends(get_current_user)):
    # Verificar se já existe funcionário vinculado à fazenda
    existente = db.query(FuncionarioModel).filter(
        FuncionarioModel.fazenda_id == funcionario.fazenda_id
    ).first()

    if existente:
        raise HTTPException(
            status_code=400,
            detail="Já existe um funcionário cadastrado para esta fazenda."
        )

    db_funcionario = FuncionarioModel(**funcionario.dict(exclude_unset=True))
    db.add(db_funcionario)
    db.commit()
    db.refresh(db_funcionario)
    return db_funcionario

@router.get("/", response_model=List[FuncionarioSchema])
def listar_funcionarios(db: Session = Depends(get_current_user)):
    return db.query(FuncionarioModel).all()
