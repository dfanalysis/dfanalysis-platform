# Domain Policy — Política de Competência

## Objetivo

A Política de Competência define as regras que determinam quando uma competência fiscal pode ser utilizada em um processo da Plataforma DF Analysis IA.

Seu objetivo é garantir que todos os processos administrativos, fiscais e financeiros respeitem os períodos de referência estabelecidos pela legislação e pelas regras operacionais da organização.

---

# Motivação

A competência é um dos conceitos centrais do domínio.

Diversos processos dependem dela, como:

* emissão de NFS-e;
* cancelamento de NFS-e;
* substituição de NFS-e;
* relatórios de produção;
* apuração de repasses;
* cálculos tributários;
* fechamento mensal;
* auditorias.

As regras relacionadas à competência não pertencem aos Aggregates nem aos Domain Services, devendo ser centralizadas em uma Policy.

---

# Responsabilidades

A Política de Competência é responsável por responder perguntas como:

* esta competência está aberta?
* esta competência pode receber novas emissões?
* esta competência pode ser alterada?
* é permitido realizar lançamentos retroativos?
* esta competência já foi encerrada?
* existe autorização para reabertura?
* esta competência pertence ao exercício correto?

---

# Escopo

A política pode ser aplicada sobre:

* Solicitação de Emissão;
* Relatório de Produção;
* NFS-e;
* Repasse Médico;
* Processo Administrativo;
* cálculos tributários;
* integrações externas.

---

# Estados da competência

Uma competência pode assumir os seguintes estados:

* Aberta;
* Em Processamento;
* Encerrada;
* Reaberta;
* Bloqueada;
* Arquivada.

---

# Regras de Negócio

A política deve garantir que:

* apenas competências abertas aceitem novos lançamentos, salvo exceções autorizadas;
* competências encerradas não sejam alteradas sem reabertura formal;
* reaberturas sejam registradas e auditadas;
* lançamentos retroativos respeitem regras específicas da organização e da legislação;
* toda competência possua período claramente definido;
* alterações preservem a rastreabilidade histórica.

---

# Exceções

A política pode permitir exceções quando:

* houver autorização formal;
* existir determinação legal;
* ocorrer correção de erro operacional;
* for necessária substituição de documento fiscal;
* existir decisão administrativa registrada.

Toda exceção deve possuir justificativa e registro de auditoria.

---

# Resultado da avaliação

A política pode produzir:

* Competência Permitida;
* Competência Permitida com Ressalvas;
* Competência Bloqueada;
* Competência Requer Autorização Especial.

---

# Relação com Domain Services

Esta Policy não altera competências.

Ela apenas determina se determinada operação pode utilizar a competência informada.

Os Domain Services utilizam essa decisão para prosseguir ou interromper o processamento.

---

# Evolução

Novas regras poderão ser adicionadas para atender:

* diferentes municípios;
* diferentes regimes tributários;
* novos processos internos;
* padrão nacional da NFS-e;
* alterações decorrentes da Reforma Tributária.

---

# Observações

A Política de Competência centraliza um dos principais mecanismos de controle temporal da Plataforma DF Analysis IA.

Sua separação como Policy garante que alterações nas regras de negócio relacionadas a períodos fiscais possam ser implementadas sem modificar Aggregates ou Domain Services, preservando a estabilidade e a evolutividade do domínio.
