# Estado Atual da Plataforma DF Analysis IA

## Última atualização

15 de julho de 2026.

## Visão geral

A Plataforma DF Analysis IA está em fase de construção da fundação arquitetural e dos primeiros domínios de negócio.

A estratégia de desenvolvimento prioriza:

1. segurança;
2. confiabilidade;
3. escalabilidade;
4. automatização;
5. simplicidade;
6. facilidade de manutenção;
7. baixo custo operacional.

O projeto evoluiu de um agente específico para emissão de NFS-e para uma plataforma modular orientada ao ciclo administrativo, operacional, fiscal, financeiro e de repasse das empresas médicas.

---

## Stack atual

### Backend

- Python 3.12;
- FastAPI;
- SQLAlchemy 2;
- Pydantic 2;
- Alembic;
- PostgreSQL;
- autenticação JWT;
- Argon2;
- RBAC.

### Infraestrutura

- Docker;
- Docker Compose;
- ambiente virtual Python;
- Git e GitHub;
- execução local em macOS;
- estrutura preparada para VPS e serviços em nuvem.

### Automação e integrações previstas

- n8n;
- Gmail;
- Microsoft Outlook;
- WhatsApp;
- Google Workspace;
- Microsoft 365;
- ISSNet;
- Ambiente Nacional da NFS-e;
- ERPs;
- bancos e conciliação financeira.

---

## Sprints concluídas

### Sprint 11 — Identity & Access

Implementações concluídas:

- cadastro estrutural de empresas;
- usuários;
- perfis;
- permissões;
- relacionamento usuário-perfil;
- relacionamento perfil-permissão;
- autenticação;
- emissão de token JWT;
- endpoint de login;
- endpoint `/auth/me`;
- validação de senha com Argon2;
- controle inicial de acesso por RBAC;
- bootstrap da plataforma;
- seeds de desenvolvimento.

### Sprint 12 — Fundação do Domínio Fiscal

Implementações concluídas:

- criação do módulo fiscal;
- separação entre domínio e provedores externos;
- definição inicial de NFS-e, RPS, DPS e solicitação de emissão;
- criação do Aggregate Root `SolicitacaoEmissao`;
- enums fiscais;
- model SQLAlchemy;
- repository;
- registro do model no `model_registry`;
- relacionamento entre empresa e solicitações de emissão;
- documentação da linguagem ubíqua fiscal;
- documentação do ciclo de vida da solicitação;
- ADR-007 — Solicitação de Emissão como Aggregate Root.

### Sprint 13 — Consolidação do Domínio Fiscal

Implementações concluídas:

- estruturação da camada de aplicação;
- caso de uso `CreateEmissionRequest`;
- caso de uso `ValidateEmissionRequest`;
- criação do `FiscalDomainService`;
- validação de empresa existente e ativa;
- validação de competência;
- validação de valor do serviço;
- validação de descrição do serviço;
- regra de idempotência;
- exceções específicas de domínio;
- máquina de estados da solicitação de emissão;
- testes manuais isolados dos casos de uso e regras de domínio;
- ADR-008 — Solicitação de Emissão como consequência operacional;
- Mapa de Domínios da Plataforma;
- `DOMAIN_MAP.md`;
- início do `EVENT_STORMING.md`.

---

## Estado do domínio Fiscal

O módulo Fiscal possui atualmente a seguinte estrutura:

```text
app/modules/fiscal/
├── enums.py
├── integracoes/
├── nfse/
├── rps/
└── solicitacoes/
    ├── application/
    │   ├── create_request.py
    │   ├── list_requests.py
    │   └── validate_request.py
    ├── domain/
    │   └── services.py
    ├── infrastructure/
    ├── exceptions.py
    ├── models.py
    ├── repository.py
    ├── router.py
    └── schemas.py

    ---

# Sprint 14 — Comunicação e Interpretação

## Objetivo

Construir o pipeline responsável por receber comunicações, armazená-las, interpretá-las e persistir o entendimento produzido pela plataforma.

---

## Módulo Operações

### Inbox

Implementado:

- InboxMessage (Aggregate Root)
- InboxAttachment (Entity)
- Repository
- Schemas
- Domain Service
- CreateInboxMessage

---

### Interpreter

Implementado:

- InterpreterEngine (Strategy)
- RuleEngine
- AIEngine
- CommunicationInterpreter
- CommunicationInterpretation
- Repository
- InterpretCommunication

---

## Decisões Arquiteturais

A IA não toma decisões de negócio.

A IA produz interpretações.

O domínio continua responsável pelas decisões operacionais.

Foi adotado o padrão Strategy para permitir múltiplos mecanismos de interpretação.

Foi criada persistência para histórico de interpretações.

A plataforma passa a separar claramente:

Comunicação

↓

Interpretação

↓

Operação

↓

Execução

---

## Situação Atual

Concluída a infraestrutura de recepção e interpretação de comunicações.

A plataforma está preparada para iniciar o domínio OperationalRequest.