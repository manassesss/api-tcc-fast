from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class Acasalamento(Base):
    __tablename__ = "acasalamentos"

    id = Column(Integer, primary_key=True, index=True)
    matriz_id = Column(Integer, ForeignKey("animais.id"), nullable=False)
    reprodutor_id = Column(Integer, ForeignKey("animais.id"), nullable=False)
    data_acasalamento = Column(Date, nullable=False)
    tipo = Column(String, nullable=False)
    indice_genetico_progênie = Column(Float, nullable=True)
    endogamia_prevista = Column(Float, nullable=True)
    observacoes = Column(String, nullable=True)

    matriz = relationship("Animal", foreign_keys=[matriz_id])
    reprodutor = relationship("Animal", foreign_keys=[reprodutor_id])
