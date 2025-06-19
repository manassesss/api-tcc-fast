from sqlalchemy import Column, Integer, String
from app.db.session import Base

class Raca(Base):
    __tablename__ = "racas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    origem = Column(String, nullable=True)
    aspectos_gerais = Column(String, nullable=True)