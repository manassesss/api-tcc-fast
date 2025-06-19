from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class MovimentacaoAnimal(Base):
    __tablename__ = "movimentacoes_animais"

    id = Column(Integer, primary_key=True, index=True)
    animal_id = Column(Integer, ForeignKey("animais.id"), nullable=False)
    peso = Column(Float, nullable=True)
    motivo_saida = Column(String, nullable=False)
    data_movimentacao = Column(Date, nullable=False)

    animal = relationship("Animal")
