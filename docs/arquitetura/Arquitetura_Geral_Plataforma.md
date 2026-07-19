# Arquitetura Geral da Plataforma DF Analysis IA

**Versão:** 1.0

---

# 1. Propósito

A Plataforma DF Analysis IA é um ecossistema de automação inteligente desenvolvido para transformar processos administrativos, financeiros, fiscais, comerciais e operacionais em fluxos automatizados, escaláveis e orientados por Inteligência Artificial.

Inicialmente, a plataforma será utilizada internamente pela DF Analysis para automatizar seus próprios processos. Posteriormente, evoluirá para um produto SaaS destinado a empresas médicas e, futuramente, a outros segmentos de mercado.

A arquitetura foi concebida para permitir expansão contínua, reutilização de componentes e independência entre módulos.

---

# 2. Visão Estratégica

A plataforma será composta por um conjunto de Agentes Especialistas.

Cada agente será responsável por um domínio específico de negócio, possuindo autonomia operacional, porém compartilhando infraestrutura, banco de dados, autenticação e mecanismos de integração.

Todos os agentes serão orquestrados por workflows desenvolvidos no n8n.

---

# 3. Objetivos

Os principais objetivos da plataforma são:

- Automatizar processos repetitivos.
- Reduzir intervenção humana.
- Diminuir erros operacionais.
- Centralizar integrações.
- Padronizar fluxos.
- Permitir expansão modular.
- Utilizar Inteligência Artificial como apoio à tomada de decisão.
- Tornar-se uma plataforma SaaS escalável.

---

# 4. Princípios Arquiteturais

Todas as decisões técnicas da plataforma deverão respeitar os seguintes princípios:

- Segurança em primeiro lugar.
- Modularização.
- Baixo acoplamento.
- Alta coesão.
- Reutilização de componentes.
- Escalabilidade horizontal.
- Observabilidade.
- Versionamento.
- Documentação contínua.
- Automação sempre que possível.

---

# 5. Arquitetura Modular

A Plataforma DF Analysis IA será organizada em módulos independentes, cada um responsável por um domínio específico de negócio.

Cada módulo possuirá:

- banco de dados próprio (schema PostgreSQL);
- workflows próprios;
- documentação própria;
- APIs específicas;
- integrações independentes;
- agentes especializados.

Essa organização reduz o acoplamento entre componentes e facilita a evolução da plataforma.

---

## CORE

Responsável pelos componentes compartilhados por toda a plataforma.

Componentes:

- Empresas
- Usuários
- Perfis
- Permissões
- Parâmetros
- Auditoria
- Certificados Digitais
- Credenciais
- Configurações Gerais

---

## FISCAL

Responsável por todos os processos fiscais.

Componentes:

- Prestadores
- Tomadores
- Serviços
- RPS
- NFS-e
- Eventos Fiscais
- ISS
- Cancelamentos
- Cartas de Correção

---

## FINANCEIRO

Responsável pelos processos financeiros.

Componentes:

- Recebimentos
- Pagamentos
- Fluxo de Caixa
- Cobrança
- Conciliação Bancária
- Centros de Custos
- Contas a Receber
- Contas a Pagar

---

## COMERCIAL

Responsável pela gestão comercial.

Componentes:

- CRM
- Leads
- Funil de Vendas
- Propostas
- Contratos
- Clientes
- Oportunidades

---

## WORKFLOW

Responsável pela automação dos processos.

Componentes:

- Workflows n8n
- Filas
- Execuções
- Agendamentos
- Logs
- Tratamento de Erros

---

## IA

Responsável pelos recursos de Inteligência Artificial.

Componentes:

- Agentes
- Prompts
- Base de Conhecimento
- RAG
- Vetorização
- Memória
- Classificação
- Extração de Dados

---

## INTEGRAÇÕES

Responsável pela comunicação com sistemas externos.

Componentes:

- ISSNET
- APIs REST
- SOAP
- ERPs
- Microsoft 365
- Google Workspace
- WhatsApp
- OpenAI

---

## DASHBOARD

Responsável pela camada analítica.

Componentes:

- Indicadores
- KPIs
- Dashboards
- Logs
- Auditoria
- Monitoramento
- Alertas

---

## Princípio de Evolução

Novos módulos poderão ser adicionados sem necessidade de alteração estrutural da plataforma.

Cada novo módulo deverá seguir os mesmos padrões arquiteturais definidos neste documento.

---

# 6. Arquitetura em Camadas

A Plataforma DF Analysis IA adotará uma arquitetura em camadas (Layered Architecture), separando responsabilidades técnicas e funcionais.

Cada camada possui responsabilidades bem definidas e comunicação controlada.

Essa abordagem reduz o acoplamento, facilita manutenção e permite evolução independente dos componentes.

---

## Camada 1 — Interface

Responsável pela interação com usuários e sistemas externos.

Exemplos:

- Portal Administrativo
- Portal do Cliente
- Portal Médico
- APIs Públicas
- Webhooks
- WhatsApp
- Aplicativos móveis (futuro)

Essa camada não implementa regras de negócio.

Sua responsabilidade é apenas receber e apresentar informações.

---

## Camada 2 — API

Responsável por disponibilizar serviços para consumidores internos e externos.

Principais responsabilidades:

- Autenticação
- Autorização
- Validação inicial
- Endpoints REST
- Webhooks
- Versionamento de APIs

Nenhuma regra de negócio crítica deverá permanecer nesta camada.

---

## Camada 3 — Orquestração

A orquestração será realizada pelo n8n.

Esta camada será responsável por:

- iniciar processos;
- executar workflows;
- controlar decisões;
- chamar APIs;
- integrar sistemas;
- tratar exceções;
- registrar logs;
- disparar notificações.

O n8n será o principal motor operacional da plataforma.

---

## Camada 4 — Serviços

Representa as regras de negócio.

Exemplos:

- emissão de NFS-e;
- cálculo de impostos;
- geração de RPS;
- validação cadastral;
- integração bancária;
- emissão de boletos;
- geração de relatórios.

Sempre que possível, as regras deverão ser reutilizáveis por vários workflows.

---

## Camada 5 — Inteligência Artificial

Responsável pelos componentes de IA.

Inclui:

- OpenAI;
- RAG;
- Base de Conhecimento;
- Classificação de documentos;
- OCR;
- Extração de informações;
- Agentes Especialistas.

A IA nunca deverá substituir regras fiscais ou regras críticas de negócio.

Seu papel será apoiar decisões, interpretar dados e automatizar atividades cognitivas.

---

## Camada 6 — Persistência

Responsável pelo armazenamento.

Banco principal:

PostgreSQL

Principais responsabilidades:

- dados transacionais;
- auditoria;
- histórico;
- configurações;
- logs;
- credenciais;
- integrações.

Toda persistência deverá ocorrer através desta camada.

---

## Camada 7 — Integrações Externas

Responsável pela comunicação com serviços externos.

Exemplos:

- ISSNET
- Padrão Nacional NFS-e
- Microsoft 365
- Google Workspace
- WhatsApp
- ERPs
- Bancos
- APIs REST
- APIs SOAP

Cada integração deverá possuir tratamento próprio de erros, autenticação e auditoria.

---

## Fluxo Geral

A comunicação entre as camadas seguirá, preferencialmente, o fluxo abaixo:

Interface

↓

API

↓

Workflow (n8n)

↓

Serviços

↓

Banco

↓

Integrações Externas

↓

Retorno ao Workflow

↓

Persistência

↓

Notificação ao Usuário

---

## Regras Arquiteturais

Nenhuma camada deverá acessar diretamente outra que não seja sua dependência imediata.

Exemplos:

Interface → API

API → Workflow

Workflow → Serviços

Serviços → Banco

Serviços → Integrações

Essa separação reduz dependências e facilita substituições futuras.

---

# 7. Ecossistema de Agentes

A Plataforma DF Analysis IA será composta por agentes especializados.

Cada agente será responsável por um domínio específico de negócio, possuindo autonomia operacional, porém compartilhando infraestrutura, banco de dados, autenticação e mecanismos de integração.

Os agentes deverão comunicar-se através de APIs, workflows e eventos, evitando dependências diretas.

---

## Agente Emissor de NFS-e

Status: Em desenvolvimento

Objetivo:

Automatizar todo o processo de emissão de Notas Fiscais de Serviços Eletrônicas.

Principais responsabilidades:

- Receber solicitações;
- Validar dados;
- Consultar integrações;
- Gerar RPS;
- Emitir NFS-e;
- Consultar situação;
- Cancelar notas;
- Registrar auditoria;
- Notificar usuários.

---

## Agente Financeiro

Status: Planejado

Objetivo:

Automatizar os processos financeiros da empresa.

Responsabilidades:

- Fluxo de caixa;
- Contas a pagar;
- Contas a receber;
- Conciliação bancária;
- Cobrança automática;
- Emissão de boletos;
- PIX;
- Relatórios financeiros.

---

## Agente Comercial

Status: Planejado

Objetivo:

Gerenciar todo o processo comercial.

Responsabilidades:

- CRM;
- Leads;
- Funil de vendas;
- Propostas;
- Contratos;
- Follow-up;
- Indicadores comerciais.

---

## Agente Atendimento

Status: Planejado

Objetivo:

Automatizar o atendimento ao cliente.

Responsabilidades:

- WhatsApp;
- Chat;
- FAQ Inteligente;
- Agendamento;
- Encaminhamento;
- Atendimento híbrido.

---

## Agente Contratos

Status: Planejado

Objetivo:

Gerenciar contratos e documentos.

Responsabilidades:

- Geração de contratos;
- Assinaturas eletrônicas;
- Versionamento;
- Renovação;
- Controle documental.

---

## Agente RH

Status: Planejado

Objetivo:

Automatizar processos administrativos relacionados a colaboradores.

Responsabilidades:

- Documentação;
- Admissões;
- Desligamentos;
- Controle de treinamentos;
- Gestão documental.

---

## Agente Gerencial

Status: Planejado

Objetivo:

Gerar inteligência para tomada de decisão.

Responsabilidades:

- Dashboards;
- KPIs;
- Indicadores;
- Relatórios executivos;
- Alertas.

---

## Agente IA

Status: Planejado

Objetivo:

Disponibilizar serviços inteligentes para todos os demais agentes.

Responsabilidades:

- Classificação;
- OCR;
- Extração de dados;
- RAG;
- Geração de texto;
- Resumos;
- Análise documental;
- Apoio à decisão.

---

## Comunicação entre Agentes

Os agentes deverão compartilhar informações utilizando mecanismos padronizados.

Preferencialmente:

- APIs REST;
- Eventos;
- Webhooks;
- Banco de dados compartilhado;
- Workflows n8n.

Nenhum agente deverá acessar diretamente a lógica interna de outro.

Toda comunicação deverá ocorrer através de interfaces bem definidas.

---

## Evolução

Novos agentes poderão ser incorporados sem necessidade de alteração estrutural da plataforma.

Cada agente deverá respeitar os princípios arquiteturais definidos neste documento.

---

# 8. Arquitetura de Dados

O PostgreSQL será o banco de dados transacional oficial da Plataforma DF Analysis IA.

Sua estrutura foi projetada para suportar crescimento contínuo, múltiplos módulos, integração entre agentes e futura operação como plataforma SaaS.

---

## Princípios

A arquitetura de dados seguirá os seguintes princípios:

- Integridade referencial.
- Normalização dos dados.
- Auditoria completa.
- Escalabilidade.
- Reutilização.
- Versionamento por migrations.
- Separação por domínios de negócio.

---

## Organização por Schemas

Cada domínio da plataforma possuirá seu próprio schema.

Schemas atualmente definidos:

### core

Entidades compartilhadas.

Exemplos:

- empresa
- usuario
- perfil
- usuario_perfil
- parametro
- credencial
- integracao

---

### fiscal

Processos fiscais.

Exemplos:

- prestador
- tomador
- servico
- rps
- nfse

---

### financeiro

Processos financeiros.

Exemplos:

- contas_receber
- contas_pagar
- fluxo_caixa
- conciliacao

---

### comercial

CRM.

Exemplos:

- cliente
- lead
- oportunidade
- proposta

---

### workflow

Controle operacional.

Exemplos:

- workflow_execucao
- fila
- agendamento
- webhook

---

### auditoria

Histórico completo.

Exemplos:

- auditoria
- log_evento
- log_integracao

---

### integracao

Persistência das integrações externas.

Exemplos:

- endpoint
- token
- certificado
- configuracao_api

---

## Modelo Multiempresa

Toda a plataforma será multiempresa.

Todas as entidades de negócio deverão possuir referência para:

empresa_id

Essa estratégia permitirá atender diversos clientes utilizando a mesma infraestrutura.

---

## Convenções

### Chaves primárias

Todas as tabelas utilizarão:

id UUID

---

### Auditoria

Sempre que aplicável:

created_at

updated_at

created_by

updated_by

---

### Exclusão lógica

Sempre que necessário:

deleted_at

deleted_by

A exclusão física deverá ser evitada.

---

### Índices

Toda chave estrangeira deverá possuir índice.

Campos frequentemente pesquisados também deverão ser indexados.

---

### Constraints

Sempre utilizar:

PRIMARY KEY

FOREIGN KEY

UNIQUE

CHECK

NOT NULL

Evitar validações apenas na aplicação.

---

### Triggers

Sempre reutilizar funções globais.

Exemplo:

fn_update_updated_at()

Evitar duplicação de código.

---

## Versionamento

Toda alteração estrutural deverá ocorrer exclusivamente através de migrations.

Nunca alterar tabelas manualmente em produção.

---

## Seeds

Os dados iniciais deverão ser mantidos em scripts independentes.

Exemplos:

- perfis padrão
- parâmetros
- configurações iniciais

---

## Evolução

Novas tabelas deverão respeitar esta arquitetura.

Alterações estruturais deverão preservar compatibilidade sempre que possível.

Mudanças incompatíveis deverão gerar nova migration documentada.

---

# 9. Arquitetura dos Workflows

Os workflows representam a camada operacional da Plataforma DF Analysis IA.

Todos os processos automatizados deverão ser implementados como workflows padronizados, versionados e documentados.

O n8n será utilizado como motor de orquestração.

---

## Identificação

Cada workflow possuirá um identificador único.

Padrão:

WF001

WF002

WF003

...

A numeração será sequencial e nunca reutilizada.

---

## Estrutura

Cada workflow deverá possuir:

workflow.json

README.md

inputs.json

outputs.json

prompts.md

CHANGELOG.md

---

## README

O README deverá conter obrigatoriamente:

- objetivo;
- responsável;
- versão;
- dependências;
- sistemas envolvidos;
- fluxograma;
- regras de negócio;
- tratamento de erros.

---

## Inputs

Toda entrada deverá ser documentada.

Exemplo:

- origem;
- formato;
- obrigatoriedade;
- validações.

---

## Outputs

Toda saída deverá ser documentada.

Exemplo:

- sucesso;
- erro;
- logs;
- notificações.

---

## Prompts

Sempre que houver IA.

Os prompts deverão permanecer separados do workflow.

Nunca embutidos diretamente no JSON do n8n.

---

## Versionamento

Toda alteração relevante deverá atualizar:

CHANGELOG.md

---

## Tratamento de Erros

Todos os workflows deverão prever:

- timeout;
- indisponibilidade externa;
- erro de autenticação;
- erro de validação;
- erro de integração;
- repetição controlada;
- rollback quando aplicável.

---

## Auditoria

Todos os workflows deverão registrar:

- início;
- término;
- duração;
- usuário;
- empresa;
- resultado;
- erro;
- payload resumido.

---

## Logs

Os logs deverão ser classificados em:

INFO

WARNING

ERROR

CRITICAL

---

## Reutilização

Fluxos comuns deverão ser transformados em Subworkflows.

Exemplos:

Autenticação

Envio de e-mail

Registro de Auditoria

Consulta de Credenciais

Criptografia

Notificações

---

## Boas Práticas

Evitar nós duplicados.

Evitar lógica complexa dentro de IFs.

Evitar SQL espalhado.

Centralizar configurações.

Padronizar nomenclaturas.

Documentar todas as alterações.