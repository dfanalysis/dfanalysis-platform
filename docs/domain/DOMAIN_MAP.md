# DOMAIN MAP
## Plataforma DF Analysis IA

> Este documento representa o mapa oficial do domínio da Plataforma DF Analysis IA.
>
> Seu objetivo é definir os Bounded Contexts, responsabilidades, fronteiras de domínio e fluxo operacional da plataforma.
>
> Todo novo módulo deverá respeitar este documento antes de qualquer implementação.

---

# Missão da Plataforma

A Plataforma DF Analysis IA tem como missão transformar o conhecimento operacional da DF Analysis em processos digitais, automatizados, auditáveis e escaláveis.

A emissão de NFS-e é apenas uma etapa de um fluxo muito maior.

---

# Princípios

- O domínio vem antes do código.
- O conhecimento do negócio é o principal ativo da plataforma.
- Nenhuma regra operacional deve ficar espalhada pelo código.
- Toda regra específica deverá ser parametrizável sempre que possível.
- Os módulos deverão possuir baixo acoplamento.
- A comunicação entre módulos deverá ocorrer preferencialmente por eventos de domínio.

---

# Bounded Contexts

## Cadastro

Responsável por:

- Empresas
- Pessoas
- Médicos
- Usuários
- Perfis
- Permissões

---

## Instituições

Responsável por:

- Grupo Hospitalar
- Instituições
- Hospitais
- Estabelecimentos
- CNPJ
- Inscrição Municipal
- Contratos Operacionais

---

## Operações

Responsável por:

- Inbox
- Emails
- Anexos
- OCR
- Classificação
- Demandas Operacionais
- Workflow

---

## Produção Médica

Responsável por:

- Produções
- Procedimentos
- Pacientes
- Médicos Executores
- Competências
- Consolidação

---

## Fiscal

Responsável por:

- Solicitação de Emissão
- RPS
- DPS
- NFS-e
- Eventos Fiscais
- Protocolos
- XML

---

## Financeiro

Responsável por:

- Contas a Receber
- Recebimentos
- Conciliação Bancária
- Baixas
- Fluxo de Caixa

---

## Repasse Médico

Responsável por:

- Grupo de Repasse
- Regras
- Rateios
- Pagamentos
- Relatórios

---

## Inteligência Artificial

Responsável por:

- Agentes
- Classificação
- Extração
- Automação
- Insights
- Recomendações

# Fluxo Principal da Plataforma

Email Recebido

↓

Anexos Importados

↓

Documentos Classificados

↓

Empresa Identificada

↓

Instituição Identificada

↓

Estabelecimento Identificado

↓

Contrato Operacional Identificado

↓

Produção Interpretada

↓

Demanda Operacional

↓

Solicitação de Emissão

↓

NFS-e Emitida

↓

Recebimento Financeiro

↓

Conciliação

↓

Grupo de Repasse

↓

Repasse Médico

↓

Processo Encerrado