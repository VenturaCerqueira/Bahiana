from fastapi import FastAPI
from database import engine, SessionLocal
import models
from routers import aluno
import seed # NOVO: Importa o módulo de seed

# Cria as tabelas no banco de dados (se não existirem)
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API da Escola Pequenas Crianças",
    description="API para gerenciar a matrícula de alunos, com operações CRUD completas.",
    version="2.0.0"
)

# NOVO: Bloco para popular o banco de dados na inicialização
@app.on_event("startup")
def on_startup():
    db = SessionLocal()
    seed.seed_db(db)
    db.close()

# Inclui o roteador de alunos na aplicação principal
app.include_router(aluno.router)

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Bem-vindo à API da Escola! Acesse /docs para ver a documentação interativa."}
