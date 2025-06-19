from sqlalchemy import Column, Integer, String
from app.db.session import Base

class Fazenda(Base):
    __tablename__ = "fazendas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    localizacao = Column(String, nullable=True)
    responsavel = Column(String, nullable=True)