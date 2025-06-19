from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class Animal(Base):
    __tablename__ = "animais"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    sexo = Column(String, nullable=False)
    data_nascimento = Column(Date, nullable=True)
    rebanho_id = Column(Integer, ForeignKey("rebanhos.id"), nullable=True)
    rebanho = relationship("Rebanho")
    indice_genetico = Column(Float, default=0.0)        # DEP / índice
                             
    pai_codigo = Column(String, nullable=True)
    mae_codigo = Column(String, nullable=True)
    categoria = Column(String, nullable=True)
    raca = Column(String, nullable=True)
    finalidade = Column(String, nullable=True)
    tipo_parto = Column(String, nullable=True)
    composicao_genetica = Column(String, nullable=True)

    data_desmame = Column(Date, nullable=True)
    peso = Column(Float, nullable=True)
    ecc = Column(Integer, nullable=True)
    conformacao = Column(Integer, nullable=True)
    precocidade = Column(Integer, nullable=True)
    musculatura = Column(Integer, nullable=True)

    altura_garupa = Column(Float, nullable=True)
    altura_paleta = Column(Float, nullable=True)
    altura_cernelha = Column(Float, nullable=True)
    comprimento_corporal = Column(Float, nullable=True)
    perimetro_toracico = Column(Float, nullable=True)

    area_olho_lombo = Column(Float, nullable=True)
    gordura_subcutanea = Column(Float, nullable=True)
    espessura_gordura = Column(Float, nullable=True)
    profundidade_olho_lombo = Column(Float, nullable=True)

    data_medição_verminose = Column(Date, nullable=True)
    opg = Column(Integer, nullable=True)
