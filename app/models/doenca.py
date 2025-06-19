from sqlalchemy import Column, Integer, String
from app.db.session import Base

class Doenca(Base):
    __tablename__ = "doencas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    causa = Column(String, nullable=False)
    profilaxia = Column(String, nullable=False)
    sintomas = Column(String, nullable=False)
    tratamento = Column(String, nullable=False)
    observacoes = Column(String, nullable=True)