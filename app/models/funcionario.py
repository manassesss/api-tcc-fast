from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class Funcionario(Base):
    __tablename__ = "funcionarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=True)
    cpf = Column(String, nullable=False)
    endereco = Column(String, nullable=False)
    municipio = Column(String, nullable=False)
    estado = Column(String, nullable=True)
    telefone = Column(String, nullable=False)

    fazenda_id = Column(Integer, ForeignKey("fazendas.id"), nullable=False)
    fazenda = relationship("Fazenda")