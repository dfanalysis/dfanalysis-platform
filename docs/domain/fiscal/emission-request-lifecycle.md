# Ciclo de Vida — Solicitação de Emissão

## Objetivo

Este documento descreve os estados válidos da Solicitação de Emissão e as transições permitidas entre eles.

## Fluxo principal

```text
RECEBIDA
    │
    ▼
EM_VALIDACAO
    │
    ▼
VALIDADA
    │
    ▼
AGUARDANDO_PROCESSAMENTO
    │
    ▼
PROCESSANDO
    ├──────────────► EMITIDA
    │
    ├──────────────► REJEITADA
    │
    └──────────────► FALHA
```

## Estados

### RECEBIDA

A solicitação foi criada e registrada na plataforma.

Ainda não houve qualquer validação.

---

### EM_VALIDACAO

As validações de negócio estão sendo executadas.

Exemplos:

- empresa ativa;
- prestador válido;
- tomador válido;
- competência;
- tributação;
- consistência dos valores.

---

### VALIDADA

Todas as validações obrigatórias foram concluídas com sucesso.

A solicitação está apta para processamento.

---

### AGUARDANDO_PROCESSAMENTO

A solicitação aguarda execução por um workflow ou fila.

---

### PROCESSANDO

A solicitação está sendo enviada ao provedor fiscal.

---

### EMITIDA

A NFS-e foi autorizada.

Estado final.

---

### REJEITADA

O provedor recusou a emissão.

Pode gerar uma nova tentativa após correção.

---

### FALHA

Erro interno da plataforma.

Não representa rejeição fiscal.

Pode ser reprocessada.

---

### CANCELADA

Solicitação encerrada sem emissão.

Utilizada quando o processo é interrompido antes da autorização fiscal.

## Regras gerais

- Toda solicitação inicia em RECEBIDA.
- Não é permitido ir diretamente de RECEBIDA para PROCESSANDO.
- Uma solicitação EMITIDA não pode retornar para VALIDADA.
- FALHA representa erro técnico.
- REJEITADA representa erro de negócio ou fiscal.
- CANCELADA encerra o ciclo da solicitação.