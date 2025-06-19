from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.manejo_schema import ManejoReprodutivo as ManejoSchema
from app.models.manejo_reprodutivo import ManejoReprodutivo as ManejoModel
from app.db.dependency import get_db
from typing import List
from app.core.deps import get_current_user        # 👈 novo

router = APIRouter(prefix="/manejos-reprodutivos", tags=["Manejo Reprodutivo"])

@router.post("/", response_model=ManejoSchema)
def criar_manejo(manejo: ManejoSchema, db: Session = Depends(get_current_user)):
    db_manejo = ManejoModel(**manejo.dict(exclude_unset=True))
    db.add(db_manejo)
    db.commit()
    db.refresh(db_manejo)
    return db_manejo

@router.get("/", response_model=List[ManejoSchema])
def listar_manejos(db: Session = Depends(get_current_user)):
    return db.query(ManejoModel).all()
