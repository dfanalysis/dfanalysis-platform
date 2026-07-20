# Aggregate — NFS-e

## Objetivo

A NFS-e representa o documento fiscal eletrônico emitido em decorrência da prestação de um ou mais serviços.

No domínio da Plataforma DF Analysis IA, a NFS-e é resultado de um processo administrativo previamente validado.

Ela não inicia um processo. Ela é consequência de uma Solicitação de Emissão.

---

# Motivação

A emissão da NFS-e é um marco importante do processo fiscal, porém não representa o início do fluxo operacional.

A plataforma trata a Nota Fiscal como um artefato fiscal derivado de uma Solicitação de Emissão previamente validada.

---

# Responsabilidades

A NFS-e é responsável por:

* representar o documento fiscal emitido;
* armazenar os dados retornados pelo município;
* manter a rastreabilidade da emissão;
* registrar cancelamentos;
* registrar substituições;
* registrar retenções;
* registrar tributos;
* permitir consultas posteriores.

---

# Identidade

Cada NFS-e possui identidade própria.

Exemplos:

* Número da NFS-e
* Código de Verificação
* Município emissor

Representação conceitual:

```text id="9kzqao"
Município + Número da NFS-e
```

---

# Estado

Uma NFS-e possui:

* número;
* série;
* código de verificação;
* data de emissão;
* competência;
* prestador;
* tomador;
* discriminação dos serviços;
* valores;
* tributos;
* retenções;
* situação;
* XML;
* PDF;
* protocolo de autorização.

---

# Situações possíveis

* Emitida
* Cancelada
* Substituída
* Rejeitada
* Denegada
* Em processamento

---

# Entidades pertencentes ao Aggregate

O Aggregate controla:

* Itens de Serviço;
* Tributos;
* Retenções;
* Arquivos XML;
* Arquivos PDF;
* Protocolos;
* Histórico Fiscal.

---

# Value Objects utilizados

* Valor Monetário;
* Competência;
* Período;
* CNPJ;
* CPF;
* Alíquota;
* Percentual;
* Inscrição Municipal.

---

# Papéis envolvidos

* Prestador;
* Tomador;
* Médico Executante.

---

# Invariantes

O Aggregate garante que:

* toda NFS-e possui um Prestador;
* toda NFS-e possui um Tomador;
* toda NFS-e possui competência definida;
* toda emissão gera XML correspondente;
* o XML representa a versão oficial do documento;
* cancelamentos preservam o histórico;
* substituições mantêm vínculo com a nota original;
* documentos fiscais não podem ser alterados após autorização.

---

# Operações do Aggregate

O Aggregate permite:

* registrarEmissao();
* registrarRetornoMunicipio();
* anexarXML();
* anexarPDF();
* registrarProtocolo();
* cancelar();
* substituir();
* consultar();
* registrarEventoFiscal().

---

# Eventos de Domínio produzidos

* NFS-e Emitida;
* XML Recebido;
* PDF Gerado;
* NFS-e Cancelada;
* NFS-e Substituída;
* Protocolo Registrado;
* Retorno Municipal Recebido.

---

# Relacionamentos

Uma NFS-e:

* pertence a uma Solicitação de Emissão;
* possui um Prestador;
* possui um Tomador;
* pode referenciar um ou mais Médicos Executantes;
* pode originar um processo de repasse;
* pode originar registros financeiros;
* pode ser utilizada em auditorias.

---

# Limites do Aggregate

A NFS-e não executa:

* autenticação no portal municipal;
* comunicação com o ISSNET;
* leitura de XML;
* geração de PDF;
* cálculo tributário;
* envio de e-mails;
* notificações.

Essas responsabilidades pertencem aos Domain Services e às integrações externas.

---

# Observações

A NFS-e representa o documento fiscal oficial emitido perante o município.

No contexto da Plataforma DF Analysis IA, ela é um artefato derivado da Solicitação de Emissão e serve como base para os módulos Financeiro, Repasse Médico, Auditoria, Relatórios, Integrações e Inteligência Artificial.
