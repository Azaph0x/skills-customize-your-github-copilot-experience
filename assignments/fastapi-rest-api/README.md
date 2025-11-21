# 📘 Assignment: APIs REST com FastAPI

## 🎯 Objetivo

Os estudantes vão construir uma API REST simples usando o framework FastAPI. A tarefa foca em criar endpoints CRUD, usar modelos Pydantic, validação, e executar a aplicação localmente com Uvicorn.

## 📝 Tasks

### 🛠️ Configurar projeto FastAPI

#### Description
Criar o ambiente do projeto, instalar dependências e verificar que a aplicação inicial consegue responder requisições.

#### Requirements
Completed program should:

- Ter um arquivo `starter-code.py` com um app FastAPI básico.
- Instruções para rodar com `uvicorn`.


### 🛠️ Implementar CRUD para um recurso `Item`

#### Description
Implementar endpoints para criar, ler (lista e individual), atualizar e deletar itens. Use um armazenamento em memória (lista/dicionário) — persistência não é necessária.

#### Requirements
Completed program should:

- Usar `pydantic` para definir o modelo `Item`.
- Endpoints: `GET /items`, `GET /items/{id}`, `POST /items`, `PUT /items/{id}`, `DELETE /items/{id}`.
- Retornar códigos HTTP apropriados (e.g., 201 para criação, 404 quando não encontrado).


### 🛠️ Validação e tratamento de erros

#### Description
Adicionar validações básicas no modelo e tratar erros com respostas legíveis.

#### Requirements
Completed program should:

- Validar campos obrigatórios e tipos no modelo Pydantic.
- Retornar mensagens de erro úteis em respostas com status apropriado.


### 🛠️ Testes básicos (opcional)

#### Description
Criar alguns testes simples que verifiquem os principais endpoints.

#### Requirements
Completed program should:

- Conter instruções para rodar testes (p.ex. usar `pytest` se você adicionar testes).


## Instruções para rodar (local)

1. Instale dependências: `pip install -r requirements.txt`
2. Rode o servidor: `uvicorn starter-code:app --reload --port 8000`
3. Abra `http://127.0.0.1:8000/docs` para ver a documentação automática do Swagger UI.

## Materiais de apoio

- [FastAPI docs](https://fastapi.tiangolo.com/)
