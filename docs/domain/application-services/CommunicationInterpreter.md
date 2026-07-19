# Application Service — CommunicationInterpreter

## Objetivo

O CommunicationInterpreter é responsável por transformar uma comunicação recebida em um entendimento estruturado.

Ele não executa regras de negócio dos domínios Fiscal, Financeiro ou Repasse.

Sua responsabilidade é exclusivamente interpretar.

---

# Entrada

InboxMessage

InboxAttachment

---

# Estratégias de interpretação

## RuleEngine

Responsável por executar regras determinísticas.

Exemplos:

- remetente conhecido;
- domínio do e-mail;
- assunto padronizado;
- palavras-chave;
- padrões hospitalares.

---

## AIEngine

Responsável pela interpretação utilizando modelos de IA.

Exemplos:

- extração semântica;
- OCR;
- classificação de documentos;
- identificação de processos;
- interpretação de anexos.

---

# Resultado

CommunicationInterpretation

---

# Responsabilidades

- interpretar comunicações;
- combinar estratégias;
- medir confiança;
- solicitar revisão humana quando necessário.

---

# Não deve

- emitir NFS-e;
- criar repasses;
- executar financeiro;
- alterar dados fiscais;
- alterar mensagens recebidas.

---

# Fluxo

InboxMessage
        │
        ▼
CommunicationInterpreter
        │
        ├── RuleEngine
        ├── AIEngine
        ▼
CommunicationInterpretation