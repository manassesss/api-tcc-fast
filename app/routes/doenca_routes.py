from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.doenca_schema import Doenca as DoencaSchema
from app.models.doenca import Doenca as DoencaModel
from app.db.dependency import get_db
from typing import List
from app.core.deps import get_current_user        # 👈 novo

router = APIRouter(prefix="/doencas", tags=["Doenças"])

@router.post("/", response_model=DoencaSchema)
def criar_doenca(doenca: DoencaSchema, db: Session = Depends(get_current_user)):
    db_doenca = DoencaModel(**doenca.dict(exclude_unset=True))
    db.add(db_doenca)
    db.commit()
    db.refresh(db_doenca)
    return db_doenca

@router.get("/", response_model=List[DoencaSchema])
def listar_doencas(db: Session = Depends(get_current_user)):
    return db.query(DoencaModel).all()