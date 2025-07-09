# API Desafio-Bahiana

## 📜 Descrição do Projeto

Esta é a versão 1.0.0 da API para o sistema de matrículas da "Escola Pequenas Crianças". Desenvolvida com FastAPI e SQLAlchemy, a API oferece uma solução completa para o gerenciamento de alunos, incluindo operações de criação, leitura, atualização e exclusão (CRUD).

O projeto também inclui um frontend simples, construído com HTML, CSS e JavaScript, que consome a API para fornecer uma interface de usuário interativa para visualizar e gerenciar os alunos.

## ✨ Funcionalidades Principais

* **API RESTful Completa**: Endpoints para todas as operações CRUD de alunos.
* **Banco de Dados**: Utiliza SQLite para armazenamento de dados, com a estrutura de tabelas gerenciada pelo SQLAlchemy.
* **Interface Frontend**: Uma página web interativa para visualizar, adicionar e deletar alunos.
* **Validação de Dados**: O Pydantic é usado para garantir a integridade e validação dos dados enviados para a API.
* **Testes Unitários**: O projeto inclui testes para garantir a confiabilidade dos endpoints da API.
* **Seed de Dados**: Um script para popular o banco de dados com dados iniciais para facilitar o desenvolvimento e os testes.
* **CORS Configurado**: Permite que o frontend, servido de um domínio diferente, acesse a API sem problemas.

## 🛠️ Tecnologias Utilizadas

* **Backend**: Python, FastAPI, SQLAlchemy
* **Banco de Dados**: SQLite
* **Frontend**: HTML, CSS, JavaScript, Bootstrap
* **Testes**: Pytest

## 🚀 Como Executar o Projeto

### Pré-requisitos

* Python 3.8 ou superior
* Um gerenciador de pacotes Python (como `pip`)

### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone <https://github.com/VenturaCerqueira/Bahiana>
    cd <Bahiana>
    ```

2.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

### Executando a Aplicação

1.  **Inicie o servidor da API:**
    A partir do diretório raiz do projeto, execute o seguinte comando:
    ```bash
    uvicorn app.main:app --reload
    ```
    O servidor estará disponível em `http://127.0.0.1:8000`.

2.  **Acesse a documentação da API:**
    Para ver a documentação interativa gerada pelo Swagger UI, acesse:
    `http://127.0.0.1:8000/docs`

3.  **Visualize o Frontend:**
    Abra o arquivo `public/view/index.html` em seu navegador para interagir com a aplicação.

## 🧪 Executando os Testes

Para rodar os testes unitários e garantir que tudo está funcionando como esperado, execute o seguinte comando na raiz do projeto:

```bash
pytest