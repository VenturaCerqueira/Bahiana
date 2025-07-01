from sqlalchemy import Column, Integer, String
from database import Base

class AlunoDB(Base):
    __tablename__ = "alunos"
    id = Column(Integer, primary_key=True, index=True)
    nome_aluno = Column(String, index=True, unique=True) # Adicionado unique para evitar nomes duplicados
    idade_aluno = Column(Integer)
    nome_responsavel = Column(String)
    turma_aluno = Column(String)