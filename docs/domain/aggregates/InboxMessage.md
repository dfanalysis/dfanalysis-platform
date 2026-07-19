# Aggregate Root — InboxMessage

## Objetivo

Representa qualquer comunicação recebida pela Plataforma DF Analysis IA.

A origem da comunicação é irrelevante para o domínio.

Pode ser:

- e-mail;
- WhatsApp;
- API;
- Webhook;
- upload manual;
- integração com ERP;
- outro canal suportado futuramente.

O Aggregate representa a entrada oficial da plataforma.

---

# Responsabilidades

- preservar a mensagem original;
- preservar metadados;
- preservar anexos;
- iniciar a rastreabilidade;
- iniciar o correlation_id;
- originar demandas operacionais.

---

# Atributos

## Identificação

- id
- correlation_id

## Origem

- canal
- origem
- message_id_externo

## Conteúdo

- assunto
- corpo

## Participantes

- remetente
- destinatarios

## Datas

- recebido_em

## Estado

- status

## Segurança

- hash_conteudo

## Relacionamentos

- empresa
- instituição
- estabelecimento

Todos inicialmente opcionais.

---

# Invariantes

- uma mensagem possui exatamente um correlation_id;
- uma mensagem nunca perde seu conteúdo original;
- uma mensagem nunca perde seus anexos;
- uma mensagem nunca troca de canal;
- uma mensagem nunca muda seu remetente original.

---

# Eventos

- EntradaRecebida
- AnexosImportados
- DocumentosClassificados
- EmpresaPrestadoraIdentificada
- DemandaOperacionalCriada

---

# Aggregate seguintes

InboxMessage

↓

InboxAttachment

↓

OperationalRequest