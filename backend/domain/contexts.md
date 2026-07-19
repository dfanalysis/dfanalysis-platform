---

id: DOMAIN-001
titulo: Contextos de Negócio da Plataforma DF Analysis IA
versao: 1.0.0
status: Em elaboração
ultima_atualizacao: 2026-07-19
responsavel: DF Analysis
------------------------

# Contextos de Negócio da Plataforma DF Analysis IA

## Objetivo

Este documento define os principais contextos de negócio da Plataforma DF Analysis IA.

Cada contexto representa uma área funcional com responsabilidades, regras, entidades e processos próprios.

A definição desses contextos orientará:

* a organização dos módulos do backend;
* a documentação do domínio;
* a criação dos agentes de Inteligência Artificial;
* a implementação de APIs e integrações;
* a separação das regras de negócio;
* a evolução modular da plataforma.

---

# 1. Núcleo da Plataforma

## Responsabilidade

Fornecer os componentes compartilhados por todos os módulos e agentes da plataforma.

## Principais capacidades

* autenticação;
* autorização;
* usuários;
* empresas;
* perfis;
* permissões;
* configurações;
* auditoria;
* logs;
* integrações;
* infraestrutura de Inteligência Artificial;
* gerenciamento de prompts;
* processamento de comunicações;
* armazenamento de evidências.

## Observação

O Núcleo não deve concentrar regras específicas dos demais contextos de negócio.

---

# 2. Faturamento

## Responsabilidade

Gerenciar o processo de emissão de documentos fiscais destinados ao recebimento pelos serviços prestados por empresas médicas.

## Escopo inicial

* recebimento de solicitações de emissão;
* identificação da empresa prestadora;
* identificação do tomador;
* validação dos dados recebidos;
* classificação da modalidade de faturamento;
* definição da competência;
* formação da descrição dos serviços;
* emissão de NFS-e;
* armazenamento de PDF, XML e protocolo;
* envio do documento emitido;
* acompanhamento do processamento.

## Principais modalidades

* produção médica apurada por hospitais;
* produção médica apurada por clínicas;
* atendimentos particulares;
* plantões;
* prestação de serviços para empresas;
* cooperativas;
* convênios diretos.

## Principais entidades

* solicitação de emissão;
* prestador;
* tomador;
* competência;
* serviço;
* descrição do serviço;
* NFS-e;
* RPS;
* protocolo;
* documento fiscal.

## Observação

Este contexto não inclui o faturamento de guias médicas perante operadoras de planos de saúde.

---

# 3. Fiscal

## Responsabilidade

Centralizar as regras tributárias e fiscais utilizadas pela plataforma.

## Principais capacidades

* validação de tributação;
* definição de alíquotas;
* retenções;
* incidência de ISS;
* enquadramento de serviços;
* códigos de atividade;
* regras municipais;
* CNAE;
* natureza da operação;
* validações fiscais da NFS-e;
* acompanhamento de alterações legais.

## Principais entidades

* regra fiscal;
* município;
* atividade;
* alíquota;
* retenção;
* tributo;
* enquadramento tributário.

## Relação com Faturamento

O contexto de Faturamento solicita ao contexto Fiscal as regras necessárias para validar e emitir documentos fiscais.

---

# 4. Financeiro

## Responsabilidade

Gerenciar os eventos financeiros relacionados às empresas atendidas pela plataforma.

## Principais capacidades

* contas a receber;
* contas a pagar;
* recebimentos;
* conciliação bancária;
* cobrança;
* inadimplência;
* fluxo de caixa;
* repasses médicos;
* distribuição de resultados;
* projeções financeiras.

## Principais entidades

* título financeiro;
* recebimento;
* pagamento;
* conta bancária;
* conciliação;
* repasse;
* cobrança;
* movimentação financeira.

## Relação com Faturamento

A emissão de uma NFS-e poderá gerar automaticamente um registro de conta a receber.

---

# 5. Comercial

## Responsabilidade

Gerenciar o relacionamento comercial da DF Analysis e das empresas atendidas.

## Principais capacidades

* gestão de leads;
* CRM;
* prospecção;
* oportunidades;
* propostas;
* negociações;
* contratos comerciais;
* follow-up;
* relacionamento com médicos;
* relacionamento com hospitais e clínicas.

## Principais entidades

* lead;
* oportunidade;
* cliente;
* contato;
* proposta;
* negociação;
* atividade comercial.

---

# 6. Administrativo

## Responsabilidade

Gerenciar processos administrativos e documentais das empresas atendidas.

## Principais capacidades

* gestão documental;
* contratos;
* procurações;
* certificados digitais;
* licenças;
* cadastros;
* credenciamentos;
* documentos societários;
* controle de vencimentos;
* rotinas administrativas.

## Principais entidades

* documento;
* contrato;
* certificado;
* licença;
* credenciamento;
* vencimento;
* cadastro.

---

# 7. Faturamento Assistencial

## Responsabilidade

Gerenciar o faturamento de atendimentos realizados por clínicas e hospitais perante operadoras de planos de saúde.

## Principais capacidades

* recebimento de guias;
* conferência de atendimentos;
* lançamento em sistema de faturamento;
* validação TISS;
* geração de XML TISS;
* formação de lotes;
* envio para portais de operadoras;
* registro de protocolos;
* acompanhamento de pagamentos;
* tratamento de glosas;
* reapresentação de contas;
* conciliação com operadoras.

## Principais entidades

* guia;
* atendimento;
* beneficiário;
* operadora;
* lote;
* XML TISS;
* protocolo;
* glosa;
* recurso de glosa;
* pagamento assistencial.

## Sistemas relacionados

* KonsistMed;
* portais das operadoras;
* sistemas clínicos;
* sistemas hospitalares.

## Observação

Este contexto é independente do contexto de Faturamento responsável pela emissão de NFS-e.

---

# 8. Business Intelligence

## Responsabilidade

Consolidar dados dos demais contextos para gerar informações gerenciais.

## Principais capacidades

* dashboards;
* indicadores;
* relatórios;
* alertas;
* análises;
* previsões;
* acompanhamento de desempenho;
* identificação de inconsistências;
* geração de insights por Inteligência Artificial.

## Fontes de dados

* Faturamento;
* Fiscal;
* Financeiro;
* Comercial;
* Administrativo;
* Faturamento Assistencial;
* Núcleo da Plataforma.

---

# Relações entre os contextos

## Fluxo principal do Agente Emissor de NFS-e

```text
Comunicação recebida
        ↓
Núcleo da Plataforma
        ↓
Faturamento
        ↓
Fiscal
        ↓
Emissão da NFS-e
        ↓
Financeiro
        ↓
Business Intelligence
```

## Fluxo futuro do Faturamento Assistencial

```text
Atendimento realizado
        ↓
Faturamento Assistencial
        ↓
Envio à operadora
        ↓
Pagamento ou glosa
        ↓
Financeiro
        ↓
Business Intelligence
```

---

# Regra de organização

Toda nova funcionalidade deverá ser associada a um contexto de negócio antes de ser implementada.

Quando uma funcionalidade envolver mais de um contexto, cada contexto deverá manter apenas as responsabilidades e regras que lhe pertencem.

Regras de negócio não devem ser duplicadas entre contextos.

---

# Contexto prioritário

O primeiro contexto priorizado para implementação completa será:

```text
Faturamento
```

O objetivo inicial será automatizar o processo de emissão de NFS-e para empresas médicas, começando pela integração com o ISSNET do Distrito Federal.
