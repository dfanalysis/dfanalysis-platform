# Roadmap — Plataforma DF Analysis IA

## Objetivo

Este documento apresenta a evolução planejada da Plataforma DF Analysis IA.

O roadmap é incremental e poderá ser refinado conforme novas regras de negócio, integrações e riscos forem identificados.

A ordem de implementação deve respeitar:

1. segurança;
2. confiabilidade;
3. escalabilidade;
4. automatização;
5. simplicidade;
6. facilidade de manutenção;
7. baixo custo operacional.

---

# Visão estratégica

A Plataforma DF Analysis IA será uma plataforma modular especializada na gestão administrativa, operacional, fiscal, financeira e de repasses de empresas médicas.

O fluxo principal será:

```text
Entrada operacional
    ↓
Produção médica
    ↓
Faturamento
    ↓
NFS-e
    ↓
Recebimento
    ↓
Repasse médico
    ↓
Auditoria e indicadores

---

# Sprint 14 — Concluída

Entrega:

- Comunicação
- Inbox
- Attachments
- Strategy Pattern
- Rule Engine
- AI Engine
- Communication Interpreter
- Communication Interpretation
- Persistência das interpretações

---

# Sprint 15

Objetivo:

Construção do domínio central da plataforma.

OperationalRequest.

Responsabilidades:

- representar uma unidade de trabalho;
- receber interpretações;
- gerar demandas operacionais;
- integrar Fiscal;
- integrar Financeiro;
- integrar Repasse;
- controlar ciclo de vida operacional.

Será o principal Aggregate Root da Plataforma DF Analysis IA.