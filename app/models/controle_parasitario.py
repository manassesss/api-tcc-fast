from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class ControleParasitario(Base):
    __tablename__ = "controles_parasitarios"

    id = Column(Integer, primary_key=True, index=True)
    animal_id = Column(Integer, ForeignKey("animais.id"), nullable=False)
    medicamento_id = Column(Integer, ForeignKey("medicamentos.id"), nullable=False)
    data_vermifugacao = Column(Date, nullable=False)
    opg_pre = Column(Integer, nullable=True)
    opg_pos = Column(Integer, nullable=True)
    escore_corporal = Column(Integer, nullable=True)
    famacha = Column(Integer, nullable=True)
    observacoes = Column(String, nullable=True)

    animal = relationship("Animal")
    medicamento = relationship("Medicamento")
