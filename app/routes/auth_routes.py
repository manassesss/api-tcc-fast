from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr

from app.db.dependency import get_db
from app.models.usuario import Usuario
from app.core.security import verify_password, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter(tags=["Auth"])

class LoginData(BaseModel):
    email: EmailStr
    senha: str

@router.post("/login")
def login(datos: LoginData, db: Session = Depends(get_db)):
    user = db.query(Usuario).filter(Usuario.email == datos.email).first()
    if not user or not verify_password(datos.senha, user.senha):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="E-mail ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(
        data={"sub": str(user.id)},
        expires_delta=ACCESS_TOKEN_EXPIRE_MINUTES
    )
    return {"access_token": access_token, "token_type": "bearer", "name": user.nome}