from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class Rebanho(Base):
    __tablename__ = "rebanhos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    descricao = Column(String, nullable=True)
    fazenda_id = Column(Integer, ForeignKey("fazendas.id"), nullable=True)
    fazenda = relationship("Fazenda")
