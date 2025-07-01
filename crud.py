from sqlalchemy.orm import Session
import models, schemas

def get_aluno(db: Session, aluno_id: int):
    return db.query(models.AlunoDB).filter(models.AlunoDB.id == aluno_id).first()


def get_aluno_by_name(db: Session, nome: str):
    return db.query(models.AlunoDB).filter(models.AlunoDB.nome_aluno == nome).first()

def get_alunos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.AlunoDB).offset(skip).limit(limit).all()

def create_aluno(db: Session, aluno: schemas.AlunoCreate):
    db_aluno = models.AlunoDB(**aluno.dict())
    db.add(db_aluno)
    db.commit()
    db.refresh(db_aluno)
    return db_aluno

def update_aluno(db: Session, aluno_id: int, aluno: schemas.AlunoCreate):
    db_aluno = db.query(models.AlunoDB).filter(models.AlunoDB.id == aluno_id).first()
    if db_aluno:
        update_data = aluno.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_aluno, key, value)
        db.commit()
        db.refresh(db_aluno)
    return db_aluno

def delete_aluno(db: Session, aluno_id: int):
    db_aluno = db.query(models.AlunoDB).filter(models.AlunoDB.id == aluno_id).first()
    if db_aluno:
        db.delete(db_aluno)
        db.commit()
    return db_aluno
