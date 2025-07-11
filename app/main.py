from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# --- AJUSTE DE IMPORTAÇÃO ---
import app.model.models as models
from app.database.database import engine, SessionLocal
from app.routers import aluno
import app.seed.seed as seed

# Cria as tabelas no banco de dados (se não existirem)
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API da Escola Pequenas Crianças",
    description="API para gerenciar a matrícula de alunos, com operações CRUD completas.",
    version="2.0.0"
)

# ======== CONFIGURAÇÃO DO CORS ========
origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ======== SEED DO BANCO DE DADOS ========
@app.on_event("startup")
def on_startup():
    db = SessionLocal()
    seed.seed_db(db)
    db.close()

# ======== INCLUSÃO DAS ROTAS ========
app.include_router(aluno.router)

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Bem-vindo à API da Escola! Acesse /docs para ver a documentação interativa."}