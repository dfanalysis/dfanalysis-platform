# Domain Service — Apuração de Repasses

## Objetivo

O Domain Service de Apuração de Repasses é responsável por calcular os valores devidos a cada Médico Executante com base na produção realizada, nas NFS-e emitidas e nas regras contratuais vigentes.

Seu objetivo é produzir uma apuração financeira consistente, auditável e reproduzível, servindo de base para o pagamento dos honorários médicos.

---

# Motivação

A apuração de repasses depende simultaneamente de informações provenientes de diferentes Aggregates e regras de negócio.

Entre elas:

* Relatório de Produção;
* NFS-e;
* Prestador;
* Médico Executante;
* Competência;
* Contratos;
* Regras de distribuição;
* Retenções;
* Ajustes financeiros.

Como o comportamento ultrapassa os limites de qualquer Aggregate, ele deve ser representado por um Domain Service.

---

# Responsabilidades

O serviço é responsável por:

* consolidar dados da produção;
* consolidar dados do faturamento;
* identificar médicos participantes;
* aplicar regras contratuais;
* calcular participações;
* calcular retenções;
* calcular descontos;
* calcular ajustes;
* gerar memória de cálculo;
* produzir o Aggregate Repasse Médico.

---

# Entradas

O serviço recebe:

* Relatório de Produção;
* NFS-e;
* Competência;
* Prestador;
* regras contratuais;
* parâmetros financeiros;
* configurações do processo.

---

# Saídas

O serviço produz:

* valores individuais;
* valores totais;
* memória de cálculo;
* inconsistências;
* Aggregate Repasse Médico;
* eventos de domínio.

---

# Fontes de cálculo

O cálculo pode utilizar:

* procedimentos realizados;
* quantidade de atendimentos;
* valores faturados;
* percentual de participação;
* valor fixo;
* rateio;
* produção individual;
* produção compartilhada;
* produtividade;
* contratos específicos.

---

# Regras de Negócio

O serviço deve garantir que:

* toda produção esteja validada;
* toda NFS-e esteja autorizada quando exigido;
* toda regra utilizada possua origem identificada;
* todo cálculo seja reproduzível;
* toda alteração gere nova memória de cálculo;
* nenhuma distribuição ultrapasse a base financeira disponível;
* toda divergência seja registrada.

---

# Fluxo conceitual

1. Receber os Aggregates de origem.
2. Consolidar dados da produção.
3. Consolidar dados fiscais.
4. Carregar regras contratuais.
5. Identificar médicos participantes.
6. Aplicar regras de distribuição.
7. Aplicar retenções e descontos.
8. Calcular valores individuais.
9. Gerar memória de cálculo.
10. Produzir o Aggregate Repasse Médico.
11. Publicar eventos de domínio.

---

# Eventos produzidos

* Apuração Iniciada;
* Participação Calculada;
* Ajuste Financeiro Aplicado;
* Memória de Cálculo Gerada;
* Repasse Apurado.

---

# Dependências

Este Domain Service pode utilizar:

* Aggregate Relatório de Produção;
* Aggregate NFS-e;
* Aggregate Repasse Médico;
* Policies de Repasse;
* Policies Contratuais;
* Policies Financeiras;
* Configurações do Prestador.

---

# Limites

Este Domain Service não:

* realiza pagamentos;
* efetua transferências bancárias;
* envia comprovantes;
* gera arquivos bancários;
* realiza integração com instituições financeiras;
* persiste diretamente os dados.

Essas responsabilidades pertencem aos módulos Financeiro, Aplicação e Infraestrutura.

---

# Memória de cálculo

Cada execução deve produzir uma memória contendo:

* versão das regras utilizadas;
* origem dos dados;
* critérios de distribuição;
* percentuais aplicados;
* retenções;
* descontos;
* ajustes;
* valores individuais;
* valor total distribuído;
* data e hora da execução.

Essa memória deve permitir a reprodução integral do cálculo em auditorias futuras.

---

# Evolução do domínio

O serviço deve permitir a coexistência de múltiplos modelos de repasse, possibilitando que diferentes Empresas Médicas utilizem regras próprias sem necessidade de alterar o domínio central.

Novas formas de cálculo devem ser incorporadas por meio de Policies e configurações.

---

# Observações

A Apuração de Repasses representa a transformação das regras financeiras e operacionais da DF Analysis em um modelo explícito de domínio.

Ao centralizar esse comportamento em um Domain Service, a Plataforma DF Analysis IA reduz dependências de planilhas, aumenta a rastreabilidade dos cálculos e cria uma base sólida para os módulos Financeiro, Gerencial, Business Intelligence e futuras integrações com sistemas bancários e ERPs.
