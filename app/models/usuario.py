from sqlalchemy import Column, Integer, String, Boolean
from app.db.session import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    id       = Column(Integer, primary_key=True, index=True)
    nome     = Column(String(60), nullable=False)
    email    = Column(String(120), unique=True, index=True, nullable=False)
    tipo     = Column(String(60), nullable=False)
    senha    = Column(String, nullable=False)               # hash!
    is_admin = Column(Boolean, default=False)
