import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Importa a aplicação principal e as dependências
from main import app
from database import Base, get_db

# Configura um banco de dados de teste em memória
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Sobrescreve a dependência get_db para usar o banco de teste
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# Cria um "cliente" de teste que podemos usar para chamar os endpoints
@pytest.fixture(scope="module")
def client():
    # Cria as tabelas no banco de teste antes de rodar os testes
    Base.metadata.create_all(bind=engine)
    yield TestClient(app)
    # Limpa as tabelas depois que os testes terminam
    Base.metadata.drop_all(bind=engine)