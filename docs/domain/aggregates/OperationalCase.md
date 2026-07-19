# Aggregate Conceitual — OperationalCase

## Objetivo

Representa um processo operacional completo da Plataforma DF Analysis IA.

Um OperationalCase nasce a partir de uma comunicação recebida e permanece ativo até que todas as etapas do processo sejam concluídas.

Ele representa a unidade central de rastreabilidade da plataforma.

---

# Origem

Pode ser iniciado por:

- e-mail;
- WhatsApp;
- API;
- webhook;
- ERP;
- upload manual;
- integração.

---

# Responsabilidades

- acompanhar o ciclo de vida operacional;
- centralizar o status do processo;
- relacionar documentos;
- relacionar interpretações;
- relacionar solicitações;
- relacionar faturamento;
- relacionar recebimentos;
- relacionar repasses;
- fornecer rastreabilidade completa.

---

# Não deve

Emitir NFS-e.

Executar financeiro.

Executar repasse.

Interpretar comunicações.

---

# Entidades relacionadas

InboxMessage

CommunicationInterpretation

SolicitacaoFaturamento

SolicitacaoEmissao

NFSe

ContaReceber

GrupoRepasse

DemonstrativoRepasse

---

# Estado do processo

Recebido

Interpretado

Em Faturamento

NF Emitida

NF Enviada

Aguardando Recebimento

Recebido

Conciliado

Repasse Liberado

Repasse Efetuado

Encerrado

Cancelado