from pydantic import BaseModel, EmailStr
from typing import Optional


# ---------- MODELOS BÁSICOS ----------
class UsuarioBase(BaseModel):
    nome: str
    email: EmailStr
    tipo: Optional[str] = None          # “admin”, “produtor”, etc.

    class Config:
        from_attributes = True          # pydantic v2 → `from_attributes`
        orm_mode = True                 # pydantic v1 (se ainda usar)


# ---------- CRIAÇÃO ----------
class UsuarioCreate(UsuarioBase):
    senha: str                          # senha *obrigatória* na criação


# ---------- LEITURA ----------
class UsuarioRead(UsuarioBase):
    id: int
    is_admin: bool                      # ou use `tipo` se preferir

    # não expomos a senha!


# ---------- ATUALIZAÇÃO ----------
class UsuarioUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[EmailStr] = None
    senha: Optional[str] = None
    tipo: Optional[str] = None
    is_admin: Optional[bool] = None     # se quiser permitir trocar

    class Config:
        from_attributes = True
