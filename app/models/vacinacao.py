from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class Vacinacao(Base):
    __tablename__ = "vacinacoes"

    id = Column(Integer, primary_key=True, index=True)
    animal_id = Column(Integer, ForeignKey("animais.id"), nullable=False)
    medicamento_id = Column(Integer, ForeignKey("medicamentos.id"), nullable=False)
    data_vacinacao = Column(Date, nullable=False)
    observacoes = Column(String, nullable=True)

    animal = relationship("Animal")
    medicamento = relationship("Medicamento")
