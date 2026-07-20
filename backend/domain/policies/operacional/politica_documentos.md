# Domain Policy — Política de Documentos

## Objetivo

A Política de Documentos define quais documentos são exigidos, opcionais ou proibidos para cada processo da Plataforma DF Analysis IA.

Seu objetivo é estabelecer critérios objetivos para a composição documental necessária à execução dos processos administrativos, fiscais e financeiros.

---

# Motivação

Cada processo pode exigir conjuntos documentais diferentes.

Por exemplo:

* emissão de NFS-e;
* cancelamento de NFS-e;
* substituição de NFS-e;
* apuração de repasses;
* auditoria;
* integração com ERP.

Essas exigências representam regras de negócio e devem permanecer centralizadas em uma Policy.

---

# Responsabilidades

A Política de Documentos é responsável por responder perguntas como:

* quais documentos são obrigatórios?
* quais documentos são opcionais?
* quais documentos são aceitos?
* quais formatos são permitidos?
* quais documentos devem ser assinados?
* quais documentos devem existir simultaneamente?
* quais documentos dependem do município?
* quais documentos dependem do tipo de serviço?

---

# Escopo

A política pode ser aplicada sobre:

* Solicitação de Emissão;
* Processo Administrativo;
* Relatório de Produção;
* NFS-e;
* Repasse Médico;
* integrações externas;
* processos futuros da plataforma.

---

# Classificação dos documentos

Cada documento pode ser classificado como:

* Obrigatório;
* Condicional;
* Opcional;
* Complementar;
* Informativo;
* Proibido.

---

# Tipos documentais

Exemplos de documentos suportados:

* Relatório de Produção;
* PDF da NFS-e;
* XML da NFS-e;
* RPS;
* Planilhas;
* Contratos;
* Guias fiscais;
* Comprovantes;
* Certificados;
* Documentos de identidade;
* Outros documentos eletrônicos.

---

# Regras de Negócio

A política deve garantir que:

* todo documento obrigatório esteja presente antes da continuidade do processo;
* documentos condicionais sejam exigidos apenas quando aplicável;
* documentos proibidos sejam rejeitados;
* formatos aceitos sejam explicitamente definidos;
* documentos duplicados possam ser identificados;
* documentos substituídos permaneçam rastreáveis;
* documentos originais nunca sejam descartados.

---

# Dependências

A obrigatoriedade de documentos pode depender de fatores como:

* município;
* Prestador;
* Tomador;
* natureza do serviço;
* regime tributário;
* tipo de processo;
* versão da integração;
* legislação vigente.

---

# Resultado da avaliação

A política pode produzir:

* documentação completa;
* documentação incompleta;
* documentação inválida;
* documentação excedente;
* documentação incompatível.

Quando houver inconsistências, todos os motivos devem ser registrados.

---

# Relação com Domain Services

Esta Policy não identifica documentos.

Também não executa validações.

Ela apenas define quais documentos devem existir para determinado contexto.

A identificação é responsabilidade do Domain Service de Identificação de Documentos.

A verificação de consistência é responsabilidade do Domain Service de Validação de Documentos.

---

# Evolução

Novos tipos documentais poderão ser adicionados sem necessidade de alterar Aggregates ou Domain Services.

A política deve permitir adaptações para:

* novos municípios;
* novos provedores de NFS-e;
* novos processos administrativos;
* integrações com ERPs;
* padrão nacional da NFS-e;
* futuras exigências da Reforma Tributária.

---

# Observações

A Política de Documentos representa o catálogo oficial de requisitos documentais da Plataforma DF Analysis IA.

Sua existência garante uniformidade entre processos, reduz inconsistências operacionais e facilita a adaptação da plataforma a diferentes cenários regulatórios e organizacionais.
