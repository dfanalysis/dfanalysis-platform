# DER — Plataforma DF Analysis IA

## Objetivo

Este documento descreve a arquitetura conceitual do banco de dados da Plataforma DF Analysis IA.

A modelagem foi desenvolvida considerando:

- arquitetura modular;
- múltiplos agentes de IA;
- múltiplas integrações;
- expansão futura da plataforma;
- reutilização de componentes.

---

# Arquitetura Geral

```
CORE
│
├── empresa
├── usuario
├── perfil
├── usuario_perfil
├── parametro
├── certificado_digital
└── ambiente

COMERCIAL
│
├── cliente
├── contato
├── contrato
└── oportunidade

FISCAL
│
├── prestador
├── tomador
├── servico
├── municipio
├── natureza_operacao
├── rps
├── lote_rps
├── nfse
├── xml_nfse
└── cancelamento_nfse

WORKFLOW
│
├── workflow
├── workflow_execucao
├── workflow_log
├── workflow_arquivo
├── fila
└── fila_execucao

INTEGRACAO
│
├── api
├── api_token
├── webhook
├── integracao
└── integracao_log

AUDITORIA
│
├── evento
├── log_sistema
├── historico
├── erro
└── auditoria_usuario

IA
│
├── agente
├── modelo_llm
├── prompt
├── prompt_versao
├── memoria
├── conversa
├── execucao_ia
└── token_consumo
```

---

# Relacionamentos principais

empresa
├── usuarios
├── parametros
├── certificados
├── clientes
├── prestadores
├── workflows
└── agentes IA

Prestador
│
└── RPS
        │
        ▼
      NFS-e
        │
        ├── XML
        ├── PDF
        └── Cancelamento

Workflow
│
└── Execuções
        │
        ├── Logs
        ├── Arquivos
        └── Integrações

Agente IA
│
├── Prompts
├── Memórias
├── Execuções
└── Consumo de Tokens

---

# Status

| Módulo | Status |
|---------|--------|
| Core | Em desenvolvimento |
| Comercial | Planejado |
| Fiscal | Planejado |
| Workflow | Planejado |
| Integrações | Planejado |
| Auditoria | Planejado |
| IA | Planejado |