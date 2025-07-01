def test_create_aluno(client):
    response = client.post(
        "/alunos/",
        json={"nome_aluno": "Aluno Teste", "idade_aluno": 5, "nome_responsavel": "Responsável Teste", "turma_aluno": "Jardim II"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["nome_aluno"] == "Aluno Teste"
    assert "id" in data

def test_read_alunos(client):
    response = client.get("/alunos/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_aluno_by_id(client):
    new_aluno_response = client.post(
        "/alunos/",
        json={"nome_aluno": "Busca Por ID", "idade_aluno": 8, "nome_responsavel": "Pai da Busca", "turma_aluno": "3A"},
    )
    aluno_id = new_aluno_response.json()["id"]

    # Agora, busca o aluno pelo ID
    response = client.get(f"/alunos/{aluno_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["nome_aluno"] == "Busca Por ID"
    assert data["id"] == aluno_id

def test_read_aluno_not_found_by_id(client):
    response = client.get("/alunos/999") # ID que não existe
    assert response.status_code == 404
    assert response.json() == {"detail": "Aluno não encontrado"}

def test_read_aluno_by_name(client):
    # Primeiro, cria um aluno para garantir que ele exista
    client.post(
        "/alunos/",
        json={"nome_aluno": "Busca Por Nome", "idade_aluno": 9, "nome_responsavel": "Mãe da Busca", "turma_aluno": "4B"},
    )

    # Agora, busca o aluno pelo nome
    response = client.get("/alunos/nome/Busca Por Nome")
    assert response.status_code == 200
    data = response.json()
    assert data["nome_aluno"] == "Busca Por Nome"

def test_read_aluno_not_found_by_name(client):
    response = client.get("/alunos/nome/Nome Inexistente")
    assert response.status_code == 404
    assert response.json() == {"detail": "Aluno não encontrado"}
