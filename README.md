## Uma API FastAPI bem feita evolui assim:

1️⃣ **Rotas e parâmetros →** como o mundo conversa com sua API
2️⃣ **Validação (Pydantic) →** garantir que os dados fazem sentido
3️⃣ **Responses / contratos →** controlar o que a API devolve
4️⃣ **CRUD + Banco →** persistência e vida real


## **PASSO 2** – Rotas, Path e Query Params (Dia 2)
🧠
➡️ Como o cliente conversa com sua API

**Exemplos:**

```
/users/1

/users/1?active=true

```

### 📌 Conceitos-chave:

Path Params → identificam um recurso

```
/users/{user_id}
```

Query Params → filtros, flags, paginação

```
?active=true
```

## 📌 PASSO 3 – Validação com Pydantic (Dia 3)
🧠 O que muda aqui?

➡️ Agora você valida dados enviados no corpo da requisição (JSON)

Antes:

qualquer coisa passa


Depois (com Pydantic):

```

{
  "name": "Ana",
  "email": "ana@email.com",
  "age": 25
}

```

## 📌 Conceitos-chave

BaseModel

Tipagem forte

Erros automáticos (422)

🎯 Objetivo real

Garantir que dados errados nunca entrem no sistema

Pydantic serve para:

validar

converter

documentar

📌 Ele não “mostra logs”
📌 Ele bloqueia erros silenciosamente

O Swagger muda porque:

FastAPI lê a assinatura da função

Gera o schema automaticamente


## PASSO 4 – CRUD + Banco (Dia 4 – parte 2)

Agora sim entra o mundo real.

🧠 O que muda?

➡️ Os dados deixam de ser “temporários”
➡️ Passam a ser persistidos

Você aprende:


- Create
- Read
- Update
- Delete

E começa a responder perguntas como:

Onde os dados ficam?

Como buscar?

Como atualizar?

## 📌 Arquitetura começa a importar

Aqui sim faz sentido separar arquivos:

```
app/
 ├── main.py        → rotas
 ├── schemas.py     → Pydantic
 ├── models.py      → Banco (ORM)
 ├── database.py   → conexão

```

📌 ANTES disso, separar arquivos atrapalha mais do que ajuda