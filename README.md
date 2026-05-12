# Extappweb

Extappweb é um projeto Django simples para gerenciamento de tarefas (to-do list) dentro da aplicação `listag`.

## Visão geral

O projeto contém:

- `manage.py`: utilitário de linha de comando Django.
- `setup/`: configuração do projeto Django, incluindo settings, URLs, WSGI e ASGI.
- `listag/`: app principal do projeto, responsável por modelar, exibir e gerenciar tarefas.
- `db.sqlite3`: banco de dados SQLite usado por padrão.

## Estrutura do projeto

### `setup/`

- `settings.py`
  - Configura o Django, incluindo apps instalados, middleware, templates, banco de dados, internacionalização e configuração do `crispy_forms`.
  - Usa `python-decouple` para carregar variáveis de ambiente como `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS` e `DATABASE_URL`.
  - Banco de dados padrão: SQLite (`db.sqlite3`).
  - Idioma definido como `pt-br` e fuso horário `America/Belem`.

- `urls.py`
  - Roteia as URLs principais do projeto.
  - Rotas cadastradas:
    - `admin/`: painel administrativo Django.
    - `/`: lista de tarefas.
    - `escola/criar/`: cria nova tarefa.
    - `escola/<int:pk>/editar/`: edita tarefa existente.
    - `escola/<int:pk>/deletar/`: exclui tarefa.
    - `escola/<int:pk>/finalizar/`: marca tarefa como concluída.

- `wsgi.py` / `asgi.py`
  - Ponto de entrada para deploys WSGI/ASGI (padrão Django).

### `listag/`

- `models.py`
  - Define o modelo `Escola` com os campos:
    - `titulo`: título da tarefa.
    - `data_criacao`: data e hora de criação automática.
    - `data_entrega`: data e hora de entrega prevista.
    - `data_finalizada`: data em que a tarefa foi concluída.
  - Adiciona método `mark_as_completed()` para marcar a tarefa como finalizada com a data atual.
  - Ordena os registros por `data_criacao`.

- `views.py`
  - `EscolaView`: exibe a lista de tarefas.
  - `EscolaCreateView`: formulário para criação de tarefas.
  - `EscolaUpdateView`: formulário para edição de tarefas.
  - `EscolaDeleteView`: confirma e exclui tarefas.
  - `EscolaCompleteView`: marca uma tarefa como concluída e redireciona para a lista.

- `admin.py`
  - Arquivo presente, mas sem registros de modelos no admin.

- `tests.py`
  - Arquivo de testes existente, ainda sem testes implementados.

### `listag/templates/`

- `base.html`
  - Template base com Bootstrap 5.
  - Cabeçalho fixo com link para a lista de tarefas.

- `listag/listag_lista.html`
  - Página principal que mostra a lista de tarefas em tabela.
  - Permite concluir, editar ou excluir cada tarefa.
  - Exibe mensagem quando não há tarefas cadastradas.
  - Link para criar nova tarefa.

- `listag/lista_form.html`
  - Formulário para criar ou editar tarefas.
  - Usa `crispy_forms` para renderizar os campos.

- `listag/lista_confirm_delete.html`
  - Página de confirmação de exclusão de tarefa.

## Funcionalidades principais

- Listar tarefas cadastradas.
- Criar nova tarefa com título e data de entrega.
- Editar tarefas existentes.
- Excluir tarefas.
- Marcar tarefas como concluídas.
- Interface responsiva com Bootstrap.

## Dependências

- Django
- python-decouple
- dj-database-url
- django-crispy-forms
- crispy-bootstrap5

## Como executar

1. Crie um ambiente virtual:

```bash
python -m venv venv
```

2. Ative o ambiente:

```powershell
venv\Scripts\Activate.ps1
```

3. Instale as dependências (adicione o `requirements.txt` se disponível) ou instale manualmente:

```bash
pip install django python-decouple dj-database-url django-crispy-forms crispy-bootstrap5
```

4. Configure variáveis de ambiente no `.env`:

```env
SECRET_KEY=chave-secreta-aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

5. Execute as migrações:

```bash
python manage.py migrate
```

6. Inicie o servidor:

```bash
python manage.py runserver
```

7. Acesse:

- `http://127.0.0.1:8000/` para a lista de tarefas
- `http://127.0.0.1:8000/admin/` para o admin Django

## Observações

- O projeto ainda não registra `Escola` em `listag/admin.py`.
- O arquivo `listag/tests.py` está disponível para adicionar testes futuros.
- A interface é construída com Bootstrap via CDN.
