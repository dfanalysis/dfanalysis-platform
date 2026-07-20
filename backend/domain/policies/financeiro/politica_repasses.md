# Domain Policy — Política de Repasses

## Objetivo

A Política de Repasses define os critérios que determinam como os valores apurados devem ser distribuídos entre os participantes de uma prestação de serviços.

Seu objetivo é centralizar as regras decisórias relacionadas à distribuição financeira, preservando a consistência, a rastreabilidade e a flexibilidade do domínio.

---

# Motivação

A distribuição de honorários médicos depende de diversos fatores.

Entre eles:

* regras contratuais;
* tipo de prestação de serviço;
* participação do Médico Executante;
* produtividade;
* rateios;
* descontos;
* retenções;
* ajustes administrativos.

Essas decisões representam políticas do domínio e não devem ficar incorporadas aos Aggregates nem aos Domain Services.

---

# Responsabilidades

A Política de Repasses é responsável por responder perguntas como:

* este médico participa do repasse?
* qual regra contratual deve ser aplicada?
* existe rateio?
* existe percentual específico?
* existem descontos obrigatórios?
* existe retenção financeira?
* existe prioridade de pagamento?
* existe bloqueio administrativo?

---

# Escopo

A política pode ser aplicada sobre:

* Relatório de Produção;
* Repasse Médico;
* Prestador;
* Médico Executante;
* Competência;
* contratos;
* parâmetros financeiros;
* regras organizacionais.

---

# Critérios de decisão

A avaliação pode considerar:

* contrato vigente;
* participação individual;
* percentual contratado;
* produtividade;
* quantidade de procedimentos;
* valor faturado;
* regras de rateio;
* retenções;
* descontos;
* ajustes extraordinários.

---

# Resultado da avaliação

A política pode produzir:

* Repasse Permitido;
* Repasse Permitido com Ajustes;
* Repasse Bloqueado;
* Repasse Requer Aprovação;
* Repasse Requer Revisão Manual.

Sempre que houver bloqueio ou exceção, todos os motivos devem ser registrados.

---

# Regras de Negócio

A política deve garantir que:

* apenas contratos vigentes sejam considerados;
* toda regra aplicada possua origem identificável;
* ajustes extraordinários sejam justificados;
* exceções sejam auditadas;
* nenhum repasse ultrapasse a base financeira disponível;
* toda decisão seja reproduzível.

---

# Exceções

A política pode permitir exceções quando:

* houver autorização administrativa;
* existir decisão contratual específica;
* houver acordo formal entre as partes;
* existir necessidade de correção operacional.

Toda exceção deve possuir justificativa e registro de auditoria.

---

# Dependências

A Política de Repasses pode depender de:

* contratos;
* parâmetros financeiros;
* regras organizacionais;
* Política de Competência;
* configurações do Prestador.

---

# Relação com Domain Services

Esta Policy não calcula valores.

Ela apenas determina quais regras deverão ser utilizadas pelo Domain Service de Apuração de Repasses.

---

# Evolução

A política deve permitir a coexistência de diferentes modelos de distribuição financeira, possibilitando que cada Empresa Médica utilize regras próprias sem necessidade de alterar o domínio central.

Novos critérios poderão ser incorporados por configuração ou novas versões da política.

---

# Observações

A Política de Repasses representa o principal mecanismo decisório do contexto financeiro da Plataforma DF Analysis IA.

Sua separação como Policy garante que alterações em contratos, percentuais ou critérios de distribuição possam ser implementadas sem modificar os Aggregates ou os Domain Services, preservando a estabilidade e a evolutividade do domínio.
