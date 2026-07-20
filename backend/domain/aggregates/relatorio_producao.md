# Aggregate — Relatório de Produção

## Objetivo

O Relatório de Produção representa o conjunto estruturado de informações que comprova a prestação de serviços realizada em um determinado período.

Ele consolida procedimentos, atendimentos, médicos executantes, valores e evidências utilizados como base para faturamento, emissão de NFS-e, auditoria e apuração financeira.

No domínio da Plataforma DF Analysis IA, o Relatório de Produção é uma das principais fontes de verdade para os processos administrativos.

---

# Motivação

Antes da emissão de uma NFS-e existe uma produção.

Essa produção normalmente é enviada pelo Hospital, Clínica ou Cooperativa por meio de:

* planilhas;
* PDFs;
* sistemas ERP;
* portais;
* e-mails;
* arquivos CSV;
* integrações.

O Relatório de Produção organiza essas informações em um único Aggregate.

---

# Responsabilidades

O Relatório de Produção é responsável por:

* consolidar a produção recebida;
* identificar médicos executantes;
* registrar procedimentos realizados;
* armazenar evidências;
* registrar competência;
* registrar período de produção;
* calcular totais operacionais;
* permitir conferência;
* servir de base para faturamento;
* servir de base para repasses.

---

# Identidade

Cada Relatório possui um identificador único.

Exemplo:

```text
RP-2026-000184
```

---

# Estado

Um Relatório de Produção possui:

* identificador;
* competência;
* período;
* prestador;
* tomador;
* lista de médicos executantes;
* lista de procedimentos;
* quantidade de atendimentos;
* valores;
* anexos;
* evidências;
* histórico;
* status.

---

# Status possíveis

* Recebido
* Em Conferência
* Validado
* Divergente
* Aprovado
* Faturado
* Encerrado

---

# Entidades pertencentes ao Aggregate

O Aggregate controla:

* Produção Médica;
* Procedimento;
* Atendimento;
* Evidência;
* Histórico;
* Divergência.

Essas entidades pertencem exclusivamente ao Relatório de Produção.

---

# Value Objects utilizados

* Competência;
* Período;
* Valor Monetário;
* Percentual;
* CRM;
* CNPJ;
* CPF.

---

# Papéis envolvidos

* Prestador;
* Tomador;
* Médico Executante;
* Solicitante.

---

# Invariantes

O Aggregate garante que:

* todo Relatório possui competência definida;
* todo procedimento pertence a um médico executante;
* toda produção pertence a um prestador;
* alterações relevantes geram histórico;
* valores consolidados devem corresponder à soma dos procedimentos;
* o Relatório somente poderá ser faturado após validação.

---

# Operações do Aggregate

O Aggregate permite:

* criar();
* importarProducao();
* adicionarProcedimento();
* removerProcedimento();
* identificarMedico();
* registrarDivergencia();
* resolverDivergencia();
* validar();
* aprovar();
* calcularTotais();
* encerrar();
* registrarHistorico().

---

# Eventos de Domínio produzidos

* Produção Importada;
* Médico Identificado;
* Procedimento Registrado;
* Divergência Encontrada;
* Divergência Resolvida;
* Relatório Validado;
* Relatório Aprovado;
* Relatório Encerrado.

---

# Relacionamentos

Um Relatório de Produção:

* pode originar uma ou mais Solicitações de Emissão;
* pode originar uma ou mais NFS-e;
* pode originar um ou mais Repasses Médicos;
* pode alimentar indicadores gerenciais;
* pode servir como evidência em auditorias.

---

# Limites do Aggregate

O Relatório de Produção não executa:

* emissão de NFS-e;
* cálculo tributário;
* comunicação com hospitais;
* integração com ERP;
* leitura de PDFs;
* OCR;
* processamento por IA.

Essas responsabilidades pertencem aos Domain Services.

---

# Observações

O Relatório de Produção representa a materialização da operação realizada pelos profissionais de saúde.

Ele estabelece a ligação entre a execução dos serviços, o faturamento, os repasses médicos e a geração de informações estratégicas para a Plataforma DF Analysis IA.

Sua modelagem permite que diferentes fontes de produção sejam tratadas de forma uniforme, preservando rastreabilidade, auditoria e consistência dos dados.
