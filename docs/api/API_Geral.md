# API Geral da Plataforma DF Analysis IA

**Versão:** 1.0

---

# Objetivo

Definir os padrões das APIs REST da plataforma.

---

# Tecnologia

Backend:

FastAPI

---

# Formato

JSON

UTF-8

HTTPS obrigatório

---

# Autenticação

JWT

OAuth2

API Keys quando necessário

---

# Versionamento

/api/v1

/api/v2

---

# Estrutura

Controllers

Services

Repositories

Schemas

Models

---

# Métodos

GET

POST

PUT

PATCH

DELETE

---

# Respostas

Sempre retornar:

status

message

data

errors

timestamp

---

# Logs

Toda requisição deverá registrar:

- usuário
- empresa
- endpoint
- duração
- IP
- resultado

---

# Segurança

Rate Limit

CORS

JWT

HTTPS

Auditoria

---

# Documentação

Swagger

OpenAPI

ReDoc

---

# Objetivos

- APIs pequenas
- Baixo acoplamento
- Alta reutilização
- Escalabilidade