# Domain Event — Competência Validada

## Objetivo

O evento **Competência Validada** representa o momento em que a competência informada para uma operação foi analisada e considerada apta para utilização no processo fiscal da Plataforma DF Analysis IA.

Esse evento confirma que o período de referência atende às regras definidas pela Política de Competência.

---

# Motivação

A competência é um dos principais elementos do domínio fiscal.

Diversas operações dependem de sua validação antes de prosseguir, como:

* emissão de NFS-e;
* substituição de NFS-e;
* cálculo tributário;
* apuração de repasses;
* fechamento mensal;
* auditorias.

Quando a competência é considerada válida, o domínio publica este evento para permitir a continuidade do processamento.

---

# Quando ocorre

O evento deve ser publicado quando:

* a competência for avaliada;
* todas as regras da Política de Competência forem atendidas;
* não existir bloqueio impeditivo para sua utilização.

Competências rejeitadas ou bloqueadas devem produzir eventos específicos.

---

# Dados do evento

O evento pode conter:

* identificador da Solicitação de Emissão;
* competência validada;
* exercício fiscal;
* período de referência;
* data e hora da validação;
* resultado da avaliação;
* versão da Política de Competência utilizada;
* responsável pela validação;
* identificador do Processo Administrativo.

O evento deve conter apenas os dados necessários para seus consumidores.

---

# Possíveis consumidores

O evento pode ser consumido por:

* Domain Service de Cálculo Tributário;
* Domain Service de Emissão de NFS-e;
* Domain Service de Auditoria;
* Domain Service de Notificação;
* módulo gerencial;
* futuros agentes especializados.

Cada consumidor decide como reagir ao evento, de forma independente.

---

# Regras de Negócio

O evento somente deve ser publicado quando:

* a competência estiver permitida para uso;
* todas as verificações obrigatórias forem concluídas;
* não houver bloqueios fiscais ou administrativos relacionados ao período.

---

# Imutabilidade

Após publicado, o evento é imutável.

Caso a competência seja posteriormente reaberta, encerrada ou alterada, novos eventos deverão ser publicados para representar esses novos fatos do domínio.

---

# Auditoria

Devem ser registrados:

* competência validada;
* exercício;
* período;
* resultado da validação;
* versão da política aplicada;
* data e hora;
* executor;
* correlação com a Solicitação de Emissão e o Processo Administrativo.

---

# Relação com o domínio

Este evento representa a confirmação de que o período fiscal está apto para utilização.

A partir dele, o domínio pode prosseguir para decisões tributárias e, posteriormente, para a autorização da emissão da NFS-e.

---

# Observações

O evento **Competência Validada** registra um dos principais marcos temporais do domínio fiscal da Plataforma DF Analysis IA.

Sua publicação garante que todos os processos subsequentes utilizem uma competência previamente aprovada pelas regras do domínio, reforçando a consistência, a rastreabilidade e a previsibilidade do fluxo operacional.
