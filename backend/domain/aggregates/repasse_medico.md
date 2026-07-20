# Aggregate — Repasse Médico

## Objetivo

O Repasse Médico representa o processo de apuração, conferência, aprovação e pagamento dos honorários devidos aos médicos executantes.

No domínio da Plataforma DF Analysis IA, o Repasse Médico consolida informações provenientes da produção médica, do faturamento e das regras financeiras para determinar os valores efetivamente devidos a cada profissional.

---

# Motivação

Após a prestação dos serviços e a emissão da NFS-e, inicia-se uma nova etapa operacional: a distribuição dos valores entre os médicos participantes.

Esse processo pode envolver:

* regras contratuais;
* participação societária;
* divisão proporcional;
* retenções;
* impostos;
* taxas administrativas;
* glosas;
* ajustes financeiros.

O Aggregate centraliza esse ciclo de negócio.

---

# Responsabilidades

O Repasse Médico é responsável por:

* consolidar valores faturados;
* identificar médicos participantes;
* aplicar regras de distribuição;
* calcular honorários;
* registrar retenções;
* registrar descontos;
* registrar ajustes;
* controlar aprovações;
* registrar pagamentos;
* manter histórico financeiro.

---

# Identidade

Cada Repasse possui um identificador único.

Exemplo:

```text
REP-2026-000087
```

---

# Estado

Um Repasse Médico possui:

* identificador;
* competência;
* período;
* prestador;
* tomador;
* relatório de produção de origem;
* NFS-e relacionadas;
* médicos participantes;
* regras de cálculo;
* valores individuais;
* retenções;
* descontos;
* ajustes;
* situação;
* histórico.

---

# Situações possíveis

* Em Apuração
* Em Conferência
* Aguardando Aprovação
* Aprovado
* Pago
* Parcialmente Pago
* Cancelado

---

# Entidades pertencentes ao Aggregate

O Aggregate controla:

* Participação Médica;
* Cálculo Individual;
* Ajuste Financeiro;
* Retenção;
* Histórico;
* Pagamento.

Essas entidades pertencem exclusivamente ao Repasse Médico.

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
* Médico Executante;
* Solicitante.

---

# Invariantes

O Aggregate garante que:

* todo Repasse pertence a uma competência;
* todo médico participante possui valor apurado;
* os valores individuais devem respeitar as regras definidas;
* o valor total distribuído deve ser consistente com a base de cálculo;
* pagamentos somente podem ocorrer após aprovação;
* toda alteração financeira gera histórico.

---

# Operações do Aggregate

O Aggregate permite:

* criar();
* adicionarParticipacao();
* removerParticipacao();
* aplicarRegraCalculo();
* recalcular();
* registrarAjuste();
* registrarRetencao();
* aprovar();
* reprovar();
* registrarPagamento();
* cancelar();
* registrarHistorico().

---

# Eventos de Domínio produzidos

* Repasse Criado;
* Participação Registrada;
* Cálculo Concluído;
* Ajuste Registrado;
* Repasse Aprovado;
* Pagamento Registrado;
* Repasse Cancelado.

---

# Relacionamentos

Um Repasse Médico:

* deriva de um Relatório de Produção;
* pode utilizar uma ou mais NFS-e como referência;
* possui um Prestador;
* envolve um ou mais Médicos Executantes;
* alimenta o módulo Financeiro;
* alimenta indicadores gerenciais.

---

# Limites do Aggregate

O Repasse Médico não executa:

* emissão de NFS-e;
* integração bancária;
* transferências financeiras;
* geração de comprovantes;
* comunicação com instituições financeiras.

Essas responsabilidades pertencem aos Domain Services e às integrações externas.

---

# Observações

O Repasse Médico representa a consolidação financeira da operação médica.

Sua modelagem permite transformar regras frequentemente mantidas em planilhas ou conhecimento tácito em um processo explícito, auditável e automatizável, servindo de base para os módulos Financeiro, Contábil, Gerencial e de Business Intelligence da Plataforma DF Analysis IA.
