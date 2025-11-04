# CRUD de Usuários com FastAPI e PostgreSQL

Este projeto implementa um sistema básico de **CRUD (Create, Read, Update, Delete)** de usuários. Ele utiliza o framework web **FastAPI** para construir a API e o **PostgreSQL** como banco de dados, com a persistência de dados gerenciada pelo **SQLAlchemy** (ou ORM similar).

A interface de administração da API está disponível via **Swagger UI** (documentação interativa automática do FastAPI).

## 🚀 Funcionalidades da API

A API possui os seguintes endpoints principais para a gestão de usuários:

| Método | Endpoint | Descrição |
| :--- | :--- | :--- |
| `GET` | `/usuarios` | Lista todos os usuários cadastrados. |
| `GET` | `/usuario/{id_usuario}` | Busca um usuário específico pelo ID. |
| `POST` | `/usuarios/cadastro` | Cadastra um novo usuário no sistema. |
| `POST` | `/usuarios/login` | Realiza o login de um usuário. |
| `PUT` | `/usuarios/atualizar/{id_usuario}` | Atualiza os dados de um usuário existente. |
| `DELETE` | `/usuarios/delete/{id_usuario}` | Remove um usuário do sistema. |

## 🛠️ Tecnologias Utilizadas

* **FastAPI:** Framework web de alta performance para APIs.
* **PostgreSQL:** Banco de dados relacional (provavelmente via `psycopg2` ou `asyncpg`).
* **SQLAlchemy / Alembic:** ORM para mapeamento objeto-relacional e migrações (se aplicável).
* **Pydantic:** Validação de dados (usado para schemas de requisição e resposta).
* **Python:** Linguagem principal do projeto.

## ⚙️ Instalação e Configuração

Siga os passos abaixo para configurar e executar o projeto em sua máquina local.

### 1. Pré-requisitos

* Python (versão 3)
* PostgreSQL (Servidor de banco de dados rodando)

### 2. Configuração do Ambiente Virtual

É altamente recomendado o uso de um ambiente virtual para isolar as dependências do projeto.

```bash
# 1. Crie o ambiente virtual (venv)
python -m venv .venv

# 2. Ative o ambiente virtual

# instale o requirements

pip install -r  requirements.txt
