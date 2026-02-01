# sissale-pdv
pdv para comércio de produtos

Passo 1 - Criação de Ambiente e instalação de dependências.

Modelo de pastas para iniciar o projeto, a fim de não confundir os caminhos:

sissale/
    backend/
    docs/
    frontend/
    README.md
___

Configurações a seguir, pós criação de pastas:

Utilizando Windows, criar ambiente .venv para iniciar o projeto, e posteriormente seguir com Docker (mais a frente):

- cd backend/py -m venv .venv
.\.venv\Scripts\Activate.ps1

Ambiente criado.

Após criado ambiente, seguir com as configurações (já disponiveis nas pastas):

back/app/main.py;
back/app/api/v1/router.py;
back/app/api/v1/endpoints/health.py;

- Rodar o servidor, ainda dentro de back (com venv ativado): uvicorn app.main:app --reload.

- Abra: http://127.0.0.1:8000/api/v1/health

Você deve ver o JSON status: ok.

Após validado, instalar: pip install fastapi uvicorn[standard]

Passo 1 Finalizado.
___

Passo 2 - Criação de Banco + ORM; Entidades-mãe; Autenticação.
