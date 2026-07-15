# ADR-008 — Solicitação de Emissão como Consequência Operacional

## Status

Aceito.

## Contexto

A Plataforma DF Analysis IA recebe demandas de faturamento por diferentes canais, principalmente e-mail, acompanhadas de relatórios, planilhas e documentos de produção médica.

Essas entradas podem conter:

- empresa prestadora;
- instituição e estabelecimento tomador;
- competência;
- período de apuração;
- processo hospitalar;
- prazo para envio da NFS-e;
- demonstrativo financeiro;
- produção analítica;
- médicos executores;
- pacientes;
- procedimentos;
- descontos;
- taxas;
- orientações para emissão.

A análise dos processos reais demonstrou que a emissão fiscal não representa o início do fluxo.

Antes dela, a plataforma precisa:

1. receber a demanda;
2. identificar o remetente e a instituição;
3. classificar os anexos;
4. identificar a empresa prestadora;
5. identificar o estabelecimento tomador;
6. interpretar a produção;
7. conferir valores;
8. aplicar regras do contrato operacional;
9. decidir se uma ou mais NFS-e devem ser emitidas.

## Decisão

A `SolicitacaoEmissao` não será o ponto de entrada da Plataforma DF Analysis IA.

Ela será criada como consequência de uma demanda operacional previamente estruturada e validada.

O fluxo conceitual será:

```text
Entrada recebida
    ↓
Demanda operacional
    ↓
Produção médica e conferência
    ↓
Decisão de faturamento
    ↓
Solicitação de emissão
    ↓
Documento provisório
    ↓
NFS-e