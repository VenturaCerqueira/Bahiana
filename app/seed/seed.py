from sqlalchemy.orm import Session
import app.crud.crud as crud, app.schemas.schemas as schemas

def seed_db(db: Session):
    # Verifica se o banco já tem dados
    alunos = crud.get_alunos(db)
    if len(alunos) > 0:
        return # Sai da função se já houver alunos

    # Dados mockados
    alunos_mock = [
        schemas.AlunoCreate(nome_aluno="Ana Zaira", idade_aluno=6, nome_responsavel="Carlos Zaira", turma_aluno="1A"),
        schemas.AlunoCreate(nome_aluno="Bruno Costa", idade_aluno=7, nome_responsavel="Fernanda Costa", turma_aluno="2C"),
        schemas.AlunoCreate(nome_aluno="Carla Dias", idade_aluno=6, nome_responsavel="Roberto Dias", turma_aluno="1A"),
    ]

    for aluno in alunos_mock:
        crud.create_aluno(db, aluno)