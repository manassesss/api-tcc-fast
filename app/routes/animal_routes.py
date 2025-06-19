
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.animal_schema import Animal as AnimalSchema
from app.models.animal import Animal as AnimalModel
from app.db.dependency import get_db
from app.core.deps import get_current_user        # 👈 novo
from typing import List

router = APIRouter(prefix="/animais", tags=["Animais"])

@router.post("/", response_model=AnimalSchema)
def criar_animal(animal: AnimalSchema, db: Session = Depends(get_current_user)):
    db_animal = AnimalModel(**animal.dict(exclude_unset=True))
    db.add(db_animal)
    db.commit()
    db.refresh(db_animal)
    return db_animal

@router.get("/", response_model=List[AnimalSchema])
def listar_animais(db: Session = Depends(get_current_user)):
    return db.query(AnimalModel).all()
