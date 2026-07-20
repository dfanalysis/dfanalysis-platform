# Aggregate — Solicitação de Emissão

## Objetivo

A Solicitação de Emissão representa o processo iniciado quando a Plataforma DF Analysis IA recebe uma solicitação para emissão de uma Nota Fiscal de Serviços Eletrônica (NFS-e).

Este Aggregate coordena todo o ciclo de vida da solicitação, desde o recebimento até sua conclusão, funcionando como o principal Aggregate Root do domínio fiscal.

---

# Motivação

Na operação da DF Analysis, o evento central não é a emissão da NFS-e.

O evento central é o recebimento de uma solicitação.

Uma solicitação pode:

* possuir documentos;
* exigir validações;
* possuir pendências;
* gerar uma ou mais NFS-e;
* falhar;
* ser cancelada;
* exigir intervenção humana.

Por esse motivo, a Solicitação de Emissão é o Aggregate Root do processo.

---

# Responsabilidades

A Solicitação de Emissão é responsável por:

* receber a solicitação;
* controlar seu ciclo de vida;
* armazenar documentos recebidos;
* controlar validações;
* controlar pendências;
* controlar aprovações;
* controlar erros;
* controlar reprocessamentos;
* controlar emissão da NFS-e;
* controlar comunicação com o solicitante;
* registrar auditoria.

---

# Identidade

Cada Solicitação possui um identificador único.

Exemplo:

```text
SOL-2026-000001
```

---

# Estado

Uma Solicitação possui:

* identificador;
* data de criação;
* competência;
* período;
* prestador;
* tomador;
* solicitante;
* documentos;
* evidências;
* observações;
* histórico;
* status.

---

# Status possíveis

* Recebida
* Em Análise
* Aguardando Complementação
* Validada
* Em Processamento
* Emitida
* Concluída
* Cancelada
* Rejeitada
* Erro

---

# Entidades pertencentes ao Aggregate

O Aggregate controla:

* Documento Recebido
* Evidência
* Histórico
* Pendência
* Validação
* Comunicação

Essas entidades não devem existir isoladamente.

Sempre pertencem à Solicitação.

---

# Value Objects utilizados

* Competência
* Período
* CNPJ
* CPF
* Valor Monetário
* Endereço
* CRM
* Inscrição Municipal

---

# Papéis envolvidos

* Prestador
* Tomador
* Solicitante
* Médico Executante

---

# Invariantes

O Aggregate garante que:

* uma Solicitação sempre possui um Prestador;
* toda Solicitação possui origem identificada;
* documentos não podem ser removidos após auditoria, apenas substituídos por nova versão;
* não pode existir emissão antes da validação;
* não pode existir conclusão antes da emissão;
* alterações relevantes devem gerar histórico;
* toda mudança de estado deve ser registrada.

---

# Operações do Aggregate

O Aggregate permite:

* criar();
* anexarDocumento();
* removerDocumento();
* validar();
* adicionarPendencia();
* removerPendencia();
* aprovar();
* rejeitar();
* iniciarProcessamento();
* emitirNFSe();
* concluir();
* cancelar();
* registrarErro();
* reprocessar();
* registrarHistorico();
* enviarNotificacao().

---

# Eventos de Domínio produzidos

* Solicitação Recebida
* Documento Anexado
* Documento Validado
* Pendência Criada
* Pendência Resolvida
* Solicitação Aprovada
* Solicitação Rejeitada
* Processamento Iniciado
* NFS-e Emitida
* Solicitação Concluída
* Solicitação Cancelada
* Erro Registrado

---

# Relacionamentos

A Solicitação pode originar:

* uma NFS-e;
* várias NFS-e;
* um Processo Administrativo;
* notificações;
* logs;
* auditorias.

---

# Limites do Aggregate

A Solicitação não executa:

* cálculo tributário;
* emissão da NFS-e;
* leitura de PDF;
* OCR;
* IA;
* acesso ao ISSNET.

Essas responsabilidades pertencem a Domain Services.

---

# Observações

A Solicitação de Emissão representa o coração operacional da Plataforma DF Analysis IA.

Todos os módulos fiscais, integrações, automações, agentes de IA e fluxos administrativos convergem para este Aggregate.

Ele será o principal ponto de orquestração do domínio fiscal.
