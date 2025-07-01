document.addEventListener('DOMContentLoaded', function () {
    const apiUrl = 'http://127.0.0.1:8000/alunos/';
    const alunosList = document.getElementById('alunos-list');
    const addAlunoForm = document.getElementById('add-aluno-form');
    const alertContainer = document.getElementById('alert-container');

    // Função para exibir alertas (continua a mesma)
    function showAlert(message, type) {
        alertContainer.innerHTML = ''; 
        const wrapper = document.createElement('div');
        wrapper.innerHTML = `
            <div class="alert alert-${type} alert-dismissible fade show" role="alert">
                ${message}
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
        `;
        alertContainer.append(wrapper);
        setTimeout(() => { wrapper.remove(); }, 5000);
    }

    // Função para buscar e exibir os alunos
    function fetchAlunos() {
        fetch(apiUrl)
            .then(response => {
                if (!response.ok) throw new Error('Falha ao carregar a lista de alunos.');
                return response.json();
            })
            .then(data => {
                alunosList.innerHTML = '';
                // MUDANÇA: colspan agora é 6
                if (data.length === 0) {
                     alunosList.innerHTML = `<tr><td colspan="6" class="text-center">Nenhum aluno matriculado.</td></tr>`;
                     return;
                }
                data.forEach(aluno => {
                    const row = document.createElement('tr');
                    // MUDANÇA: Adicionado botão de Visualizar
                    row.innerHTML = `
                        <td>${aluno.id}</td>
                        <td>${aluno.nome_aluno}</td>
                        <td>${aluno.idade_aluno}</td>
                        <td>${aluno.nome_responsavel}</td>
                        <td>${aluno.turma_aluno}</td>
                        <td class="text-center">
                            <button class="btn btn-info btn-sm" onclick="viewAluno(${aluno.id})" data-bs-toggle="modal" data-bs-target="#alunoModal" title="Visualizar">
                                <i class="bi bi-eye-fill"></i>
                            </button>
                            <button class="btn btn-danger btn-sm" onclick="deleteAluno(${aluno.id})" title="Deletar">
                                <i class="bi bi-trash-fill"></i>
                            </button>
                        </td>
                    `;
                    alunosList.appendChild(row);
                });
            })
            .catch(error => {
                console.error('Erro ao buscar alunos:', error);
                // MUDANÇA: colspan agora é 6
                alunosList.innerHTML = `<tr><td colspan="6" class="text-center text-danger">
                    <strong>${error.message}</strong> Verifique se a API está em execução.
                </td></tr>`;
            });
    }

    // Função para adicionar um novo aluno (continua a mesma)
    addAlunoForm.addEventListener('submit', function (event) {
        event.preventDefault();
        const novoAluno = {
            nome_aluno: document.getElementById('nome').value,
            idade_aluno: parseInt(document.getElementById('idade').value),
            nome_responsavel: document.getElementById('responsavel').value,
            turma_aluno: document.getElementById('turma').value,
        };
        fetch(apiUrl, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(novoAluno),
        })
        .then(response => {
            if (!response.ok) return response.json().then(err => { throw new Error(err.detail || 'Erro desconhecido.') });
            return response.json();
        })
        .then(() => {
            showAlert('Aluno adicionado com sucesso!', 'success');
            fetchAlunos();
            addAlunoForm.reset();
        })
        .catch(error => {
            showAlert(`Erro ao adicionar aluno: ${error.message}`, 'danger');
        });
    });

    // NOVO: Função para buscar dados de um aluno e preencher a modal
    window.viewAluno = function(id) {
        fetch(`${apiUrl}${id}`)
            .then(response => {
                if (!response.ok) throw new Error('Aluno não encontrado.');
                return response.json();
            })
            .then(data => {
                document.getElementById('modal-aluno-id').textContent = data.id;
                document.getElementById('modal-aluno-nome').textContent = data.nome_aluno;
                document.getElementById('modal-aluno-idade').textContent = data.idade_aluno;
                document.getElementById('modal-aluno-responsavel').textContent = data.nome_responsavel;
                document.getElementById('modal-aluno-turma').textContent = data.turma_aluno;
            })
            .catch(error => {
                console.error('Erro ao buscar dados do aluno:', error);
                showAlert(error.message, 'danger');
            });
    }

    // Função para deletar um aluno
    window.deleteAluno = function (id) {
        if (confirm('Tem certeza que deseja deletar este aluno?')) {
            fetch(`${apiUrl}${id}`, { method: 'DELETE' })
            .then(response => {
                if (!response.ok) throw new Error('Não foi possível deletar o aluno.');
                showAlert('Aluno deletado com sucesso!', 'success');
                fetchAlunos();
            })
            .catch(error => { showAlert(`Erro: ${error.message}`, 'danger'); });
        }
    };

    // Chamada inicial para carregar os alunos
    fetchAlunos();
});