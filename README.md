# fastapi_monolito

Uma aplicação de exemplo construída com FastAPI que demonstra um pequeno CRUD de usuários. Esta versão é intencionalmente simples e serve como ponto de partida para evoluções (persistência com SQLAlchemy, autenticação, validações adicionais, etc).

## Sumário
- [Recursos](#recursos)
- [Tecnologias](#tecnologias)
- [Pré-requisitos](#pré-requisitos)
- [Instalação e execução](#instalação-e-execução)
- [Endpoints da API](#endpoints-da-api)
- [Modelos e Schemas](#modelos-e-schemas)
- [Banco de dados](#banco-de-dados)
- [Testes](#testes)
- [Contribuição](#contribuição)
- [Licença](#licença)
- [Autor](#autor)

## Recursos
- Criar usuário (POST /users)
- Listar usuários (GET /users)
- Estrutura mínima com FastAPI, Pydantic e SQLAlchemy
- Scripts de teste simples incluídos

## Tecnologias
- Python
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic
- Loguru (log)

## Pré-requisitos
- Python 3.8+
- pip

## Instalação e execução

1. Clone o repositório:
```bash
git clone https://github.com/analaurafra/fastapi_monolito.git
cd fastapi_monolito
```

2. Recomenda-se criar um ambiente virtual e instalar dependências:
```bash
python -m venv .venv
source .venv/bin/activate    # macOS / Linux
# .venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

3. Execute a aplicação:
```bash
uvicorn main:app --reload
```

A API ficará disponível por padrão em http://127.0.0.1:8000. A documentação automática do FastAPI pode ser acessada em:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Endpoints da API

- POST /users
  - Descrição: cria um novo usuário
  - Body (JSON):
    ```json
    {
      "name": "João",
      "email": "joao@example.com",
      "age": 30
    }
    ```
  - Resposta: retorna o usuário criado (no formato definido em `schemas.UserCreate` / `schemas.UserResponse`)

- GET /users
  - Descrição: retorna a lista de usuários
  - Resposta: array de usuários

Exemplo usando curl:
```bash
curl -X POST "http://127.0.0.1:8000/users" -H "Content-Type: application/json" -d '{"name":"Maria","email":"maria@example.com","age":25}'
```

## Modelos e Schemas
- models.py
  - Classe `User` (SQLAlchemy): id, name, email, age
- schemas.py
  - `UserCreate` (Pydantic): name, email, age
  - `UserResponse` (herda de UserCreate e adiciona id)

Observação: o arquivo `crud.py` atualmente usa uma lista em memória (`fake_users_db`) para armazenar usuários. Isso significa que os dados não persistem entre reinícios da aplicação. A estrutura já contém `database.py` e `models.py` com SQLAlchemy para facilitar a migração para persistência real.

## Banco de dados
- `database.py` aponta para SQLite local em `sqlite:///./test.db`.
- Atualmente o CRUD utilizado pelo endpoint adiciona dados a uma lista em memória. Se desejar, posso integrar `crud.py` para usar a sessão SQLAlchemy e persistir no `test.db`.

## Testes
Existem scripts simples de teste no repositório:
- `test_request.py`
- `test_post_temp.py`

Você pode executá-los (após iniciar o servidor) com:
```bash
python test_request.py
# ou
python test_post_temp.py
```

(Dependendo do conteúdo dos scripts, pode ser necessário instalar bibliotecas extras como `requests`. Se quiser, eu posso revisar e adaptar os scripts para pytest.)

## Contribuição
Contribuições são bem-vindas. Para contribuir:
1. Fork e clone o repositório
2. Crie uma branch com a sua feature/fix: `git checkout -b feature/nome-da-feature`
3. Faça commits claros e envie um PR

## Licença
Veja o arquivo `LICENSE` no repositório para detalhes sobre a licença.

## Autor
Repositório: [analaurafra/fastapi_monolito](https://github.com/analaurafra/fastapi_monolito)
Contato: perfil GitHub do autor.
