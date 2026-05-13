# Extappweb

Extappweb é um projeto Django para gerenciamento de Relatórios Diários de Obra (RDO) na aplicação `listag`.

## Visão geral

O projeto contém:

- `manage.py`: utilitário de linha de comando Django.
- `setup/`: configuração do projeto, incluindo settings, URLs, WSGI e ASGI.
- `listag/`: app principal que gerencia o modelo `RDO`.
- `requirements.txt`: dependências fixas do projeto.
- `.env.example`: exemplo de variáveis de ambiente.

## Melhorias recentes

- Adicionado `requirements.txt` para instalação fácil de dependências.
- Adicionado `.env.example` para padronizar a configuração local.
- Atualizado `README.md` com instruções claras de instalação e execução.
- Garantido que `db.sqlite3` seja ignorado pelo Git via `.gitignore`.
- Adicionados scripts de suporte:
  - `migrate.py`
  - `start_rdo.py`
  - `01_migrate.bat`
  - `02_runserver.bat`
  - `run_test.bat`
- Removidos arquivos binários e de cache (`__pycache__`, `.pyc`) do controle de versão.
- Implementada geração de PDF para relatórios RDO com `reportlab`.
- Configuração de upload de foto para cada RDO.
- Uso de `crispy_forms` com `bootstrap5` para formulários mais elegantes.
- Criação de dashboard com métricas de RDOs totais, funcionários e registros da última semana.

## Estrutura do projeto

### `setup/`

- `settings.py`
  - Configura o Django, apps, middleware, templates, banco de dados e internacionalização.
  - Carrega variáveis de ambiente com `python-decouple`.
  - Suporta `DATABASE_URL` via `dj_database_url`.
  - Usa `pt-br` e `America/Belem`.
  - Define `MEDIA_ROOT` e `MEDIA_URL` para uploads de fotos.

- `urls.py`
  - Rotas principais do projeto:
    - `admin/`
    - `/`
    - `rdo/`
    - `rdo/criar/`
    - `rdo/<int:pk>/`
    - `rdo/<int:pk>/editar/`
    - `rdo/<int:pk>/deletar/`
    - `rdo/<int:pk>/pdf/`

- `wsgi.py` / `asgi.py`
  - Pontos de entrada padrão para deploy.

### `listag/`

- `models.py`
  - Define o modelo `RDO` com campos como:
    - `obra`
    - `responsavel`
    - `descricao`
    - `data`
    - `clima`
    - `funcionarios`
    - `observacoes`
    - `foto`
  - Inclui timestamps de criação e atualização.
  - Ordena por data de forma decrescente.

- `views.py`
  - `DashboardView` mostra métricas gerais de RDO.
  - `RDOListView` lista registros com paginação.
  - `RDOCreateView` cria novos relatórios.
  - `RDOUpdateView` edita relatórios existentes.
  - `RDODeleteView` exclui relatórios.
  - `RDODetailView` exibe detalhes de um RDO.
  - `RDOPdfView` exporta o relatório para PDF.

- `forms.py`
  - `RDOForm` usa `crispy_forms` e layout Bootstrap 5.
  - Campos configurados para datas, texto e upload de imagens.

- `admin.py`
  - Registra `RDO` no admin Django.

## Funcionalidades principais

- Painel dashboard com métricas de RDO.
- Criação, edição e exclusão de relatórios de obra.
- Visualização detalhada de cada RDO.
- Exportação de RDO para PDF.
- Upload de foto por relatório.
- Formulários Bootstrap com `crispy_forms`.
- Banco de dados local SQLite como padrão.

## Dependências

- Django
- python-decouple
- dj-database-url
- django-crispy-forms
- crispy-bootstrap5
- reportlab
- Pillow

## Como executar

1. Crie um ambiente virtual:

```bash
python -m venv venv
```

2. Ative o ambiente:

```powershell
venv\Scripts\Activate.ps1
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Configure variáveis de ambiente copiando `.env.example` para `.env`:

```bash
copy .env.example .env
```

5. Edite `.env` conforme necessário:

```env
SECRET_KEY=chave-secreta-aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

6. Execute as migrações:

```bash
python manage.py migrate
```

7. Inicie o servidor:

```bash
python manage.py runserver
```

8. Acesse:

- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/admin/`

## Observações

- `db.sqlite3` é um banco local e não deve ser versionado.
- Use `.env` para configurações sensíveis e locais.
- É recomendado não commitar arquivos de cache Python (`__pycache__`, `.pyc`).
