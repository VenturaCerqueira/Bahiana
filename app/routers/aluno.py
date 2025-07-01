from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

# --- AJUSTE DE IMPORTAÇÃO ---
from app.crud import crud
from app.schemas import schemas
from app.database.database import get_db

router = APIRouter(prefix="/alunos", tags=["Alunos"])

@router.post("/", response_model=schemas.Aluno, status_code=status.HTTP_201_CREATED)
def create_aluno_endpoint(aluno: schemas.AlunoCreate, db: Session = Depends(get_db)):
    db_aluno = crud.get_aluno_by_name(db, nome=aluno.nome_aluno)
    if db_aluno:
        raise HTTPException(status_code=400, detail="Já existe um aluno com este nome.")
    return crud.create_aluno(db=db, aluno=aluno)

@router.get("/", response_model=List[schemas.Aluno])
def read_alunos_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_alunos(db, skip=skip, limit=limit)

@router.get("/{aluno_id}", response_model=schemas.Aluno)
def read_aluno_endpoint(aluno_id: int, db: Session = Depends(get_db)):
    db_aluno = crud.get_aluno(db, aluno_id=aluno_id)
    if db_aluno is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return db_aluno

@router.get("/nome/{nome_aluno}", response_model=schemas.Aluno)
def read_aluno_by_name_endpoint(nome_aluno: str, db: Session = Depends(get_db)):
    db_aluno = crud.get_aluno_by_name(db, nome=nome_aluno)
    if db_aluno is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return db_aluno

@router.put("/{aluno_id}", response_model=schemas.Aluno)
def update_aluno_endpoint(aluno_id: int, aluno: schemas.AlunoCreate, db: Session = Depends(get_db)):
    db_aluno = crud.update_aluno(db, aluno_id=aluno_id, aluno=aluno)
    if db_aluno is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return db_aluno

@router.delete("/{aluno_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_aluno_endpoint(aluno_id: int, db: Session = Depends(get_db)):
    db_aluno = crud.delete_aluno(db, aluno_id=aluno_id)
    if not db_aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return {"ok": True}