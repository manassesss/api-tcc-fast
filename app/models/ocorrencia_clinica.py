from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class OcorrenciaClinica(Base):
    __tablename__ = "ocorrencias_clinicas"

    id = Column(Integer, primary_key=True, index=True)
    animal_id = Column(Integer, ForeignKey("animais.id"), nullable=False)
    doenca_id = Column(Integer, ForeignKey("doencas.id"), nullable=False)
    data_ocorrencia = Column(Date, nullable=False)
    observacoes = Column(String, nullable=True)

    animal = relationship("Animal")
    doenca = relationship("Doenca")