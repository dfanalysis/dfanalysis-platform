# Domain Service — Cálculo Tributário

## Objetivo

O Domain Service de Cálculo Tributário é responsável por determinar os tributos incidentes sobre uma prestação de serviços, aplicando a legislação vigente, as regras municipais e as configurações tributárias do Prestador.

Seu objetivo é produzir um resultado tributário consistente e auditável, independentemente do município ou do provedor da NFS-e.

---

# Motivação

O cálculo tributário não pertence a nenhum Aggregate específico.

Ele depende simultaneamente de informações provenientes de diferentes partes do domínio, como:

* Prestador;
* Tomador;
* Competência;
* Natureza do serviço;
* Município;
* Regime tributário;
* Valores;
* Legislação vigente.

Por essa razão, deve ser modelado como um Domain Service.

---

# Responsabilidades

O serviço é responsável por:

* identificar a legislação aplicável;
* determinar a incidência tributária;
* calcular impostos;
* calcular retenções;
* calcular deduções;
* calcular bases de cálculo;
* aplicar alíquotas;
* aplicar regras de arredondamento;
* produzir memória de cálculo;
* disponibilizar o resultado para emissão da NFS-e.

---

# Entradas

O serviço recebe:

* Solicitação de Emissão;
* Prestador;
* Tomador;
* Competência;
* Município;
* Natureza do serviço;
* Regime tributário;
* Valor dos serviços;
* Configuração tributária.

---

# Saídas

O serviço produz:

* base de cálculo;
* tributos incidentes;
* retenções;
* deduções;
* valor líquido;
* memória de cálculo;
* eventos de domínio.

---

# Tributos suportados

O modelo deve ser extensível para suportar:

* ISS;
* IRRF;
* INSS;
* PIS;
* COFINS;
* CSLL;
* IBS;
* CBS;
* outros tributos futuros.

---

# Regras de Negócio

O serviço deve garantir que:

* apenas regras vigentes sejam aplicadas;
* toda alíquota possua origem identificada;
* toda retenção possua justificativa;
* arredondamentos sejam explícitos;
* a memória de cálculo seja preservada;
* alterações legislativas não exijam mudanças nos Aggregates.

---

# Fluxo conceitual

1. Receber dados fiscais.
2. Identificar legislação aplicável.
3. Determinar tributos incidentes.
4. Calcular bases.
5. Aplicar alíquotas.
6. Aplicar retenções.
7. Aplicar deduções.
8. Calcular valor líquido.
9. Gerar memória de cálculo.
10. Disponibilizar resultado ao processo de emissão.

---

# Eventos produzidos

* Cálculo Tributário Iniciado;
* Tributos Calculados;
* Retenção Aplicada;
* Memória de Cálculo Gerada.

---

# Dependências

Este Domain Service pode utilizar:

* Aggregate Solicitação de Emissão;
* Aggregate NFS-e;
* Policies Tributárias;
* Policies Municipais;
* Tabelas de legislação;
* Configuração tributária do Prestador.

---

# Limites

Este Domain Service não:

* emite NFS-e;
* transmite XML;
* consulta portais municipais;
* executa autenticação;
* gera PDF;
* realiza persistência em banco de dados.

Essas responsabilidades pertencem às camadas de Aplicação e Infraestrutura.

---

# Memória de cálculo

Toda execução deve produzir uma memória de cálculo contendo:

* versão da regra aplicada;
* legislação utilizada;
* alíquotas;
* bases de cálculo;
* retenções;
* deduções;
* arredondamentos;
* resultado final.

Essa memória deve ser preservada para auditoria e rastreabilidade.

---

# Evolução do domínio

O serviço deve ser preparado para suportar múltiplos regimes tributários e mudanças legislativas sem impactar os Aggregates.

Novas regras devem ser incorporadas por meio de Policies e configurações, preservando a estabilidade do modelo de domínio.

---

# Observações

O Cálculo Tributário representa um dos principais pontos de variação da Plataforma DF Analysis IA.

Ao isolá-lo em um Domain Service independente, o domínio permanece desacoplado das particularidades de cada município, provedor ou legislação, permitindo que a plataforma evolua continuamente para novos cenários fiscais, incluindo a Reforma Tributária e futuras integrações nacionais.
