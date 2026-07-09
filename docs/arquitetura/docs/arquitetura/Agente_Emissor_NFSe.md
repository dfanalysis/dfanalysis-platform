# Agente Emissor de NFS-e

**Versão:** 1.0  
**Status:** Em desenvolvimento  
**Responsável:** DF Analysis

---

# Objetivo

Automatizar integralmente o processo de emissão de Notas Fiscais de Serviços Eletrônicas (NFS-e), reduzindo intervenção humana, aumentando a confiabilidade e permitindo expansão para qualquer município brasileiro.

---

# Escopo da Versão 1

Inicialmente o agente atenderá:

- ISSNET Distrito Federal
- Emissão individual de NFS-e
- Empresas clientes da DF Analysis
- Integração com PostgreSQL
- Orquestração pelo n8n

---

# Entradas

O agente deverá receber:

- Empresa emissora
- Prestador
- Tomador
- Serviço
- Valor
- Competência
- Data da emissão
- Observações
- Anexos (futuro)

---

# Validações

Antes da emissão o agente deverá validar:

- Empresa ativa
- Certificado digital válido
- Credenciais do ISSNET
- Prestador cadastrado
- Tomador cadastrado
- Serviço válido
- Município
- CNAE
- Alíquota
- Regime tributário

Caso qualquer validação falhe, o processo será interrompido.

---

# Fluxo Macro

Receber solicitação

↓

Validar dados

↓

Consultar banco

↓

Consultar integrações

↓

Autenticar no ISSNET

↓

Emitir RPS

↓

Converter em NFS-e

↓

Salvar XML

↓

Salvar PDF

↓

Atualizar banco

↓

Registrar auditoria

↓

Notificar usuário

---

# Sistemas Integrados

- PostgreSQL
- n8n
- ISSNET
- OpenAI
- WhatsApp (Evolution API)
- Microsoft 365
- Google Workspace

---

# Banco de Dados

Principais tabelas envolvidas:

## Core

- empresa
- usuario
- perfil
- parametro
- integracao
- credencial
- certificado
- auditoria

## Fiscal

- prestador
- tomador
- servico
- rps
- lote
- nfse

---

# Workflows n8n

WF001 - Recepção da solicitação

WF002 - Validação

WF003 - Emissão ISSNET

WF004 - Persistência

WF005 - Notificações

WF006 - Tratamento de erros

---

# IA

A IA será utilizada para:

- validar documentos
- interpretar e-mails
- interpretar PDFs
- interpretar XML
- responder usuários
- gerar logs explicativos
- auxiliar tratamento de exceções

A emissão fiscal continuará obedecendo rigorosamente às regras tributárias; a IA atuará como apoio à automação e à tomada de decisão, não como substituta das validações obrigatórias.

---

# Logs

Todo evento deverá ser registrado.

Exemplos:

- Solicitação recebida
- Validação iniciada
- Emissão iniciada
- Emissão concluída
- Falha de autenticação
- Erro ISSNET
- Timeout
- Cancelamento

---

# Objetivos

- Reduzir trabalho manual
- Eliminar retrabalho
- Garantir rastreabilidade
- Permitir processamento em lote
- Preparar expansão nacional
- Servir como base para futuros agentes da plataforma