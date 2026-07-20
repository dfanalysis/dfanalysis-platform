# Domain Policy — Política de Validação

## Objetivo

A Política de Validação define os critérios utilizados para determinar se uma informação, documento, entidade ou processo atende aos requisitos mínimos para prosseguir no fluxo de negócio da Plataforma DF Analysis IA.

Seu papel é concentrar decisões relacionadas à aceitação ou rejeição de elementos do domínio, mantendo essas regras desacopladas dos Aggregates e dos Domain Services.

---

# Motivação

Diversos componentes do domínio dependem de validações antes de executarem seus comportamentos.

Exemplos:

* documentos obrigatórios;
* entidades cadastradas;
* competência;
* dados fiscais;
* vínculos entre participantes;
* consistência financeira.

Essas regras representam políticas de negócio e não devem ficar distribuídas pelo sistema.

---

# Responsabilidades

A Política de Validação é responsável por responder perguntas como:

* esta informação é válida?
* este documento pode ser utilizado?
* existe alguma inconsistência impeditiva?
* a divergência encontrada bloqueia o processo?
* existe alguma exceção permitida?
* a validação exige revisão humana?

---

# Escopo

A política pode ser aplicada sobre:

* documentos;
* entidades;
* Aggregates;
* Value Objects;
* dados extraídos por IA;
* informações provenientes de integrações;
* dados informados manualmente.

---

# Resultado da avaliação

A avaliação poderá resultar em:

* Válido;
* Válido com Ressalvas;
* Pendente;
* Inválido.

Quando o resultado não for "Válido", todos os motivos devem ser registrados.

---

# Critérios de validação

Entre os critérios que podem ser avaliados estão:

* obrigatoriedade;
* completude;
* consistência;
* autenticidade;
* integridade;
* legibilidade;
* temporalidade;
* conformidade cadastral;
* conformidade fiscal;
* conformidade financeira;
* coerência entre documentos.

---

# Regras de Negócio

A política deve garantir que:

* toda validação possua critérios explícitos;
* toda reprovação possua justificativa;
* divergências sejam classificadas por severidade;
* exceções sejam registradas;
* validações automatizadas informem sua origem;
* validações por IA registrem o nível de confiança.

---

# Classificação das divergências

As divergências podem ser classificadas como:

* Informativa;
* Baixa;
* Média;
* Alta;
* Crítica.

Somente divergências classificadas como impeditivas devem bloquear automaticamente o processo.

---

# Relação com Domain Services

Esta Policy não executa validações.

Ela apenas define os critérios que serão utilizados pelo Domain Service de Validação de Documentos e por outros serviços do domínio.

---

# Evolução

Novos critérios poderão ser incorporados sem alterar os Aggregates, permitindo que a plataforma acompanhe mudanças legais, operacionais e organizacionais.

---

# Observações

A Política de Validação centraliza as decisões relacionadas à aceitação ou rejeição de informações dentro do domínio.

Essa separação reduz duplicidade de regras, facilita testes, melhora a rastreabilidade e mantém os comportamentos de validação consistentes em toda a Plataforma DF Analysis IA.
