# ADR-009

# IA interpreta. O domínio decide.

## Status

Accepted

---

## Contexto

A Plataforma DF Analysis IA utilizará modelos de Inteligência Artificial para interpretar comunicações recebidas.

Essas interpretações poderão identificar:

- empresa;
- instituição;
- estabelecimento;
- competência;
- tipo de processo;
- documentos;
- demais informações operacionais.

Entretanto, decisões críticas de negócio não devem ser delegadas diretamente aos modelos de IA.

---

## Decisão

A IA produzirá apenas interpretações estruturadas.

As decisões operacionais permanecerão sob responsabilidade do domínio.

A sequência oficial passa a ser:

InboxMessage

↓

CommunicationInterpreter

↓

CommunicationInterpretation

↓

OperationalRequest

↓

Domínios especializados

---

## Consequências

Benefícios:

- rastreabilidade;
- auditoria;
- possibilidade de reinterpretação;
- desacoplamento entre IA e negócio;
- facilidade para substituir modelos de IA;
- maior segurança operacional.

Esta decisão torna a IA um mecanismo de apoio à decisão, e não a autoridade sobre o domínio.