from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class ManejoReprodutivo(Base):
    __tablename__ = "manejos_reprodutivos"

    id = Column(Integer, primary_key=True, index=True)
    rebanho_id = Column(Integer, ForeignKey("rebanhos.id"), nullable=False)
    matriz_id = Column(Integer, ForeignKey("animais.id"), nullable=False)
    reprodutor_id = Column(Integer, ForeignKey("animais.id"), nullable=False)

    data_cobertura = Column(Date, nullable=False)
    peso_matriz = Column(Float, nullable=True)
    escore_matriz = Column(Integer, nullable=True)
    perimetro_escrotal = Column(Float, nullable=True)

    paricao_status = Column(String, nullable=True)  # sim, nao, em andamento
    data_parto = Column(Date, nullable=True)
    tipo_parto = Column(String, nullable=True) 
    data_desmame = Column(Date, nullable=True)

    observacoes = Column(String, nullable=True)

    rebanho = relationship("Rebanho")
    matriz = relationship("Animal", foreign_keys=[matriz_id])
    reprodutor = relationship("Animal", foreign_keys=[reprodutor_id])
