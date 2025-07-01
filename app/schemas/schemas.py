from pydantic import BaseModel

# Não precisa de List aqui, pois não está a ser usado.

class AlunoCreate(BaseModel):
    nome_aluno: str
    idade_aluno: int
    nome_responsavel: str
    turma_aluno: str

class Aluno(AlunoCreate):
    id: int

    class Config:
        from_attributes = True # Correção de 'orm_mode' para 'from_attributes'