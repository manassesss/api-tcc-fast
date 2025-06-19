from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.usuario_schema import UsuarioRead, UsuarioCreate, UsuarioUpdate
from app.models.usuario import Usuario as UsuarioModel
from app.db.dependency import get_db
from typing import List
from app.core.security import hash_password

router = APIRouter(prefix="/usuarios", tags=["Usuários"])

@router.post("/usuarios/", response_model=UsuarioRead)
def criar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    novo = UsuarioModel(
        nome=usuario.nome,
        email=usuario.email,
        senha=hash_password(usuario.senha),
        tipo=usuario.tipo,
        is_admin=(usuario.tipo == "admin"),
    )
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@router.get("/", response_model=List[UsuarioRead])
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(UsuarioModel).all()