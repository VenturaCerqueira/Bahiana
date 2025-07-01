from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # Certifique-se que esta linha existe

import app.model.models as models
from app.database import engine, SessionLocal
from routers import aluno
import app.seed.seed as seed

# Cria as tabelas no banco de dados (se não existirem)
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API da Escola Pequenas Crianças",
    description="API para gerenciar a matrícula de alunos, com operações CRUD completas.",
    version="2.0.0"
)

# ======== INÍCIO DA CONFIGURAÇÃO DO CORS ========
# Este bloco DEVE vir ANTES de qualquer `app.include_router`

origins = [
    "http://127.0.0.1:5500",  # Endereço do seu front-end (Live Server)
    "http://localhost:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Permite TODOS os métodos (GET, POST, OPTIONS, etc)
    allow_headers=["*"],  # Permite TODOS os cabeçalhos
)

# ======== FIM DA CONFIGURAÇÃO DO CORS ========


# Bloco para popular o banco de dados na inicialização
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