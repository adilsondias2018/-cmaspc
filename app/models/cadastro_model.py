from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, Integer, String


@dataclass
class Cadastro(db.Model):

    id: int
    nome: str
    email: str
    


    __tablename__ = "cadastro"

    id = Column(Integer, primary_key=True)

    nome = Column(String(255), nullable=False)
    dataNascimento = Column(String(20), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    cpf = Column(String(20), nullable=False, unique=True)
    identidade = Column(String(20), nullable=False, unique=True)
    telefone = Column(String(20), nullable=False)
    segmentoAtuacao = Column(String(20), nullable=False)
    tipoSegmento = Column(String(20), nullable=False)
    participacao = Column(String(), nullable=False)
    conselheiro = Column(String(3), nullable=False)
    candidato = Column(String(3), nullable=False)
    eixos = Column(String(6),nullable=False)
    termo = Column(String(6), nullable=False)



