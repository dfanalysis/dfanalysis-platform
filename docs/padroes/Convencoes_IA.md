# Convenções de Inteligência Artificial da Plataforma DF Analysis IA

**Versão:** 1.0

---

# Objetivo

Este documento estabelece os padrões oficiais para desenvolvimento dos Agentes de Inteligência Artificial da Plataforma DF Analysis IA.

Todos os agentes deverão seguir estas convenções.

---

# Filosofia

Os agentes de IA deverão atuar como especialistas em processos de negócio.

A IA não substituirá as regras de negócio da aplicação.

A IA auxiliará na interpretação, decisão e geração de conteúdo.

As regras críticas permanecerão implementadas no Backend.

---

# Arquitetura

Todo agente deverá ser composto por cinco camadas.

1. Interface
2. Orquestração
3. Inteligência
4. Ferramentas
5. Persistência

---

# Interface

Os agentes poderão receber solicitações através de:

- WhatsApp
- Portal Web
- API REST
- Webhooks
- E-mail
- Microsoft Teams
- Google Workspace

---

# Orquestração

A orquestração será realizada preferencialmente pelo n8n.

Responsabilidades:

- controlar fluxos;
- chamar ferramentas;
- registrar auditoria;
- tratar exceções;
- integrar sistemas.

---

# Inteligência

A camada de IA será responsável por:

- interpretar linguagem natural;
- classificar solicitações;
- resumir documentos;
- responder perguntas;
- apoiar decisões.

---

# Ferramentas

Todo agente deverá utilizar ferramentas específicas.

Exemplos:

- Banco de Dados
- APIs REST
- APIs SOAP
- PostgreSQL
- OpenAI
- OCR
- Busca Vetorial
- E-mail
- WhatsApp
- Calendário
- Arquivos

---

# Memória

Sempre que necessário, utilizar memória persistente.

Tipos:

- memória da conversa;
- memória operacional;
- memória organizacional.

---

# Prompts

Prompts deverão permanecer separados do código.

Nunca armazenar prompts diretamente na aplicação.

Cada agente deverá possuir:

prompt do sistema

prompt operacional

prompt de validação

prompt de fallback

---

# Versionamento

Toda alteração relevante em prompts deverá ser registrada.

---

# Modelos

A plataforma deverá permitir troca de modelos LLM sem alterar a arquitetura.

Os modelos deverão ser abstraídos.

---

# Segurança

Nunca enviar informações sensíveis sem necessidade.

Prompts não deverão conter:

- senhas;
- tokens;
- chaves privadas;
- credenciais.

---

# Auditoria

Toda interação deverá registrar:

- data;
- usuário;
- empresa;
- agente;
- modelo utilizado;
- duração;
- custo estimado;
- resultado.

---

# Hallucination

Toda resposta crítica deverá ser validada.

A IA não poderá executar ações irreversíveis sem validação.

---

# RAG

Sempre que possível utilizar Retrieval Augmented Generation.

A IA deverá consultar:

- banco de dados;
- documentos;
- manuais;
- procedimentos internos.

Evitar respostas exclusivamente baseadas no conhecimento do modelo.

---

# Ferramentas Externas

As integrações deverão ocorrer através de APIs ou serviços controlados.

Evitar acesso direto quando houver camada intermediária disponível.

---

# Especialização

Cada agente deverá possuir domínio específico.

Exemplos:

Agente Fiscal

Agente Financeiro

Agente Comercial

Agente RH

Agente Jurídico

Agente Contratos

Agente Atendimento

---

# Escalabilidade

Os agentes deverão compartilhar componentes reutilizáveis.

Exemplos:

Autenticação

Auditoria

OCR

Busca Vetorial

Banco

Logs

Notificações

---

# Checklist

Antes da publicação verificar:

- O agente possui objetivo definido?
- Existem ferramentas suficientes?
- Há validação das respostas?
- Os prompts estão documentados?
- Existe auditoria?
- Existe controle de custos?
- Existe fallback?
- Existe tratamento de erros?