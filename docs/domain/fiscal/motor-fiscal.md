# Motor Fiscal

## Objetivo

O Motor Fiscal é o núcleo responsável pelo processamento completo da emissão de Notas Fiscais de Serviço Eletrônicas (NFS-e) da Plataforma DF Analysis IA.

Seu objetivo é transformar documentos operacionais recebidos da empresa em uma NFS-e autorizada pelo município, preservando rastreabilidade, idempotência, auditoria e independência do provedor municipal.

---

# Fluxo Geral

```text
Entrada

↓

Inbox

↓

Evidências

↓

Interpretação IA

↓

Solicitação de Emissão

↓

Validação

↓

RPS

↓

Lote

↓

ISSNET

↓

NFS-e

↓

Persistência

↓

Notificações
```

---

# Aggregates

O domínio fiscal é composto inicialmente por:

- Solicitação de Emissão
- RPS
- Lote de RPS
- NFS-e

As responsabilidades de cada aggregate estão definidas no ADR-010.

---

# Princípios

O Motor Fiscal deve garantir:

- rastreabilidade;
- idempotência;
- auditoria;
- desacoplamento do provedor;
- processamento resiliente;
- recuperação de falhas;
- suporte futuro a múltiplos municípios.

---

# Próximas Capacidades

As capacidades serão implementadas incrementalmente:

- Solicitação de Emissão ✅
- Validação ✅
- Aggregate RPS
- Modelo Canônico
- Adaptador ISSNET
- XML
- Envio
- Recepção
- Persistência da NFS-e
- Auditoria