# Convenções n8n da Plataforma DF Analysis IA

**Versão:** 1.0

---

# Objetivo

Este documento estabelece os padrões para desenvolvimento de workflows na Plataforma DF Analysis IA.

Todos os workflows deverão seguir estas convenções.

---

# Filosofia

O n8n será utilizado exclusivamente como orquestrador.

As regras de negócio deverão permanecer preferencialmente no Backend (FastAPI).

O workflow deverá coordenar serviços, não concentrar lógica complexa.

---

# Estrutura

Cada workflow possuirá sua própria pasta.

Exemplo:

WF001-Emissao-NFSe/

WF002-Cancelamento-NFSe/

WF003-Consulta-NFSe/

---

# Conteúdo da pasta

Cada workflow deverá conter:

workflow.json

README.md

inputs.json

outputs.json

prompts.md

CHANGELOG.md

---

# Identificação

Todo workflow receberá um identificador único.

Formato:

WF001

WF002

WF003

A numeração nunca deverá ser reutilizada.

---

# Nome

Utilizar sempre nomes objetivos.

Exemplos:

Emitir NFSe

Cancelar NFSe

Consultar Prestador

Enviar WhatsApp

Evitar nomes genéricos.

---

# Organização dos Nós

Sempre organizar os nós da esquerda para a direita.

Separar visualmente os blocos.

Utilizar comentários quando necessário.

---

# Nome dos Nós

Os nomes deverão descrever claramente sua função.

Exemplos:

Receber Webhook

Validar Payload

Consultar Empresa

Gerar RPS

Enviar ISSNET

Registrar Auditoria

---

# Subworkflows

Funcionalidades reutilizáveis deverão ser transformadas em subworkflows.

Exemplos:

Autenticação

Auditoria

Envio de Email

Envio de WhatsApp

Consulta de Credenciais

Criptografia

---

# Variáveis

Nunca utilizar valores fixos.

Sempre utilizar:

Credenciais

Variáveis de ambiente

Parâmetros

Banco de dados

---

# Credenciais

Nunca armazenar senhas no workflow.

Utilizar o gerenciamento de credenciais do n8n.

Quando necessário, buscar credenciais criptografadas no banco.

---

# Tratamento de Erros

Todo workflow deverá possuir fluxo de erro.

Prever:

timeout

erro HTTP

erro SOAP

erro OAuth

erro de validação

erro interno

---

# Retry

Toda integração externa deverá possuir política de repetição controlada.

Evitar loops infinitos.

---

# Logs

Todo workflow deverá registrar:

início

fim

tempo de execução

empresa

usuário

workflow

resultado

erro

---

# Auditoria

Toda execução relevante deverá gerar registro na tabela de auditoria.

---

# Prompts

Prompts de IA nunca deverão ficar embutidos no JSON do workflow.

Devem permanecer em:

prompts.md

ou

Backend

---

# Performance

Evitar workflows muito grandes.

Sempre dividir processos complexos em subworkflows.

---

# Versionamento

Toda alteração deverá atualizar:

CHANGELOG.md

---

# Exportação

Sempre manter o workflow exportado em JSON dentro do repositório Git.

---

# Documentação

Todo workflow deverá possuir:

objetivo

fluxograma

dependências

entradas

saídas

tratamento de erros

limitações

---

# Checklist

Antes de concluir um workflow verificar:

- Todos os nós possuem nomes claros?
- Existem credenciais hardcoded?
- Há tratamento de erros?
- Existe documentação?
- Existe auditoria?
- Existe registro de logs?
- O workflow pode ser reutilizado?
- Existe algum nó duplicado?
- Os prompts estão separados?