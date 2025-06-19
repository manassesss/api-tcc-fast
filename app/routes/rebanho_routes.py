
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.rebanho_schema import Rebanho as RebanhoSchema
from app.models.rebanho import Rebanho as RebanhoModel
from app.db.dependency import get_db
from typing import List
from app.core.deps import get_current_user        # 👈 novo

router = APIRouter(prefix="/rebanhos", tags=["Rebanhos"])

@router.post("/", response_model=RebanhoSchema)
def criar_rebanho(rebanho: RebanhoSchema, db: Session = Depends(get_current_user)):
    db_rebanho = RebanhoModel(**rebanho.dict(exclude_unset=True))
    db.add(db_rebanho)
    db.commit()
    db.refresh(db_rebanho)
    return db_rebanho

@router.get("/", response_model=List[RebanhoSchema])
def listar_rebanhos(db: Session = Depends(get_current_user)):
    return db.query(RebanhoModel).all()
