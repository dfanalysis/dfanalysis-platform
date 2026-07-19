# DF Analysis IA Platform

> Plataforma SaaS para automação inteligente de processos administrativos, fiscais, financeiros e comerciais utilizando Inteligência Artificial, APIs REST e Agentes Especializados.

---

# Visão Geral

A **DF Analysis IA Platform** é uma plataforma modular desenvolvida para automatizar processos empresariais complexos por meio de Inteligência Artificial, integração entre sistemas e automação de workflows.

O projeto nasceu a partir da experiência prática da **DF Analysis**, empresa especializada na gestão administrativa, financeira, comercial, contábil e fiscal de empresas médicas.

Ao longo dos anos foram identificados diversos processos repetitivos, suscetíveis a erros e altamente dependentes de intervenção humana. A Plataforma DF Analysis IA tem como objetivo transformar esse conhecimento operacional em componentes reutilizáveis, automatizados e escaláveis.

O primeiro agente em desenvolvimento é o **Agente Emissor de NFS-e**, responsável por interpretar documentos, validar informações fiscais e realizar a emissão automática de Notas Fiscais de Serviço Eletrônicas.

---

# Objetivos da Plataforma

- Automatizar processos administrativos
- Automatizar processos fiscais
- Automatizar processos financeiros
- Automatizar processos comerciais
- Integrar ERPs
- Integrar ISSNET
- Integrar OpenAI
- Integrar n8n
- Disponibilizar APIs REST
- Centralizar logs e auditoria
- Criar um ecossistema de Agentes de IA especializados

---

# Arquitetura

A Plataforma segue uma arquitetura em camadas inspirada em Domain Driven Design (DDD), Clean Architecture e princípios SOLID.

```
                    HTTP / REST
                         │
                  FastAPI Router
                         │
                  Application Layer
                         │
                 Domain Services
                         │
                  Repository Layer
                         │
             SQLAlchemy / PostgreSQL
```

Cada domínio é desenvolvido de forma independente, permitindo alta reutilização e facilidade de manutenção.

---

# Tecnologias

## Backend

- Python 3.13
- FastAPI
- SQLAlchemy 2
- Alembic
- PostgreSQL
- Pydantic v2

## Segurança

- JWT
- Argon2
- RBAC (Role Based Access Control)

## Infraestrutura

- Docker
- Docker Compose
- Git
- GitHub

## Automação

- n8n
- APIs REST
- Webhooks

## Inteligência Artificial

- OpenAI
- GPT
- Interpretação de documentos
- Extração estruturada de informações

---

# Estrutura do Projeto

```
backend/
│
├── app/
│   ├── core/
│   ├── db/
│   ├── modules/
│   │
│   ├── auth/
│   ├── empresas/
│   ├── fiscal/
│   ├── operacoes/
│   └── workflow/
│
├── tests/
│
├── alembic/
│
└── main.py

database/
docker/
docs/
scripts/
workflows/
```

---

# Organização do Banco de Dados

A Plataforma utiliza PostgreSQL organizado em múltiplos schemas.

| Schema | Responsabilidade |
|---------|------------------|
| core | Empresas, Usuários, Perfis e Permissões |
| fiscal | Solicitações de emissão, NFS-e e RPS |
| operacoes | Inbox, Documentos, Casos Operacionais e Interpretação |

Essa separação facilita a evolução da plataforma sem acoplamento entre domínios.

---

# Funcionalidades Implementadas

## Infraestrutura

- SQLAlchemy
- Session Factory
- Dependency Injection
- Alembic
- Versionamento do Banco
- Logging

---

## Segurança

- Login JWT
- Refresh Token
- RBAC
- Perfis
- Permissões
- Autorização por domínio

---

## Empresas

- Cadastro
- Repository
- Domain Model
- Serviços de consulta

---

## Fiscal

Primeiro domínio completo implementado.

### Solicitações de Emissão

Implementado:

- Criação
- Consulta por ID
- Listagem
- Persistência PostgreSQL
- Repository
- Application Layer
- Domain Validation
- Controle de Idempotência
- Correlation ID

---

## Operações

Implementado:

- InboxMessage
- InboxAttachment
- OperationalCase
- CommunicationInterpretation

Esses componentes serão utilizados pelos agentes responsáveis pela interpretação automática de documentos.

---

# API REST

Documentação automática disponível em:

```
http://localhost:8000/docs
```

Principais endpoints:

```
POST /auth/login

GET /auth/me

POST /fiscal/solicitacoes

GET /fiscal/solicitacoes

GET /fiscal/solicitacoes/{id}
```

---

# Estado Atual da Plataforma

## Concluído

- Arquitetura Base
- PostgreSQL
- Alembic
- SQLAlchemy
- Autenticação JWT
- RBAC
- Empresas
- Primeiro Domínio Fiscal
- Persistência End-to-End
- API REST
- Swagger

---

# Marcos da Plataforma

| Versão | Marco |
|--------|-------|
| v0.1.0 | Infraestrutura Base |
| v0.2.0 | Autenticação + RBAC |
| **v0.3.0** | **Primeiro fluxo completo HTTP → PostgreSQL (Solicitação de Emissão)** |

---

# Roadmap

## Sprint 29

Consultas Avançadas

- Paginação
- Ordenação
- Filtros

---

## Sprint 30

Máquina de Estados

```
Recebida

↓

Em Validação

↓

Validada

↓

Aguardando Processamento

↓

Processando

↓

Emitida
```

---

## Sprint 31

Inbox

```
Email

↓

InboxMessage

↓

InboxAttachment

↓

Evidence Bundle

↓

Solicitação de Emissão
```

---

## Sprint 32

IA

```
PDF

↓

GPT

↓

Extração Estruturada

↓

Solicitação de Emissão
```

---

## Sprint 33

Integração ISSNET

- Login
- Consulta
- Emissão
- Download XML
- Download PDF

---

## Sprint 34

Workflow n8n

- Recepção automática
- Processamento
- IA
- Emissão
- Notificações
- Logs

---

# Banco de Dados

## Instalar toda a estrutura

```bash
psql -U dfanalysis -d dfanalysis -f database/schema/install.sql
```

---

## Resetar ambiente

```bash
psql -U dfanalysis -d dfanalysis -f database/schema/reset.sql
```

---

# Docker

Subir ambiente completo:

```bash
docker compose up -d
```

Parar ambiente:

```bash
docker compose down
```

---

# Testes

Executar testes:

```bash
pytest
```

---

# Visão Estratégica

A Plataforma DF Analysis IA não foi concebida para resolver apenas um processo específico.

Ela será a base para um ecossistema de Agentes de Inteligência Artificial especializados.

Agentes previstos:

- Agente Fiscal
- Agente Comercial
- Agente Financeiro
- Agente de Cobrança
- Agente de Recursos Humanos
- Agente de Contratos
- Agente Gerencial
- Agente de Atendimento

Todos compartilharão a mesma infraestrutura de autenticação, banco de dados, APIs, auditoria, workflow e inteligência artificial.

---

# Licença

© DF Analysis Tecnologia

Projeto proprietário.

Todos os direitos reservados.