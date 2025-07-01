from pydantic import BaseModel
from typing import List

class AlunoCreate(BaseModel):
    nome_aluno: str
    idade_aluno: int
    nome_responsavel: str
    turma_aluno: str

class Aluno(AlunoCreate):
    id: int
    class Config:
        orm_mode = True