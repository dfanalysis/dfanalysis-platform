# Communication Interpretation Pipeline

## Objetivo

Definir oficialmente o pipeline responsável por transformar comunicações e documentos não estruturados em informações operacionais estruturadas para a Plataforma DF Analysis IA.

Este pipeline será utilizado por todos os Agentes da plataforma.

Sua função é transformar qualquer comunicação recebida em um resultado padronizado, auditável e rastreável.

---

# Princípios Arquiteturais

O pipeline deverá seguir os seguintes princípios:

- preservar as evidências originais;
- priorizar mecanismos determinísticos;
- utilizar IA apenas quando necessário;
- produzir sempre um único contrato de saída;
- manter rastreabilidade completa;
- permitir revisão humana;
- ser independente do modelo de IA utilizado.

---

# Papel da Inteligência Artificial

A Inteligência Artificial não é responsável pelas decisões de negócio.

Sua responsabilidade é:

- interpretar informações ambíguas;
- complementar informações ausentes;
- enriquecer semanticamente os dados;
- aumentar a confiança da interpretação.

A IA nunca deverá substituir:

- regras de domínio;
- validações;
- parsers estruturados;
- decisões críticas.

---

# Visão Geral

O fluxo oficial será:

```text
InboxMessage
        ↓
EvidenceBundle
        ↓
Document Identification
        ↓
Deterministic Parsing
        ↓
Normalization
        ↓
Consolidation
        ↓
Operational Classification
        ↓
AI Enrichment
        ↓
Business Validation
        ↓
InterpreterResult
        ↓
CommunicationInterpretation
        ↓
OperationalCase
```

---

# Entrada do Pipeline

A entrada oficial do pipeline será sempre um:

```text
InboxMessage
```

Uma comunicação poderá possuir:

- nenhum anexo;
- um único anexo;
- diversos anexos;
- anexos de diferentes formatos.

Exemplos:

- e-mail contendo PDF;
- e-mail contendo XML;
- e-mail contendo Excel;
- e-mail contendo ZIP;
- upload manual;
- API;
- WhatsApp;
- Portal.

Independentemente da origem, o pipeline sempre receberá um único objeto de entrada.

---

# Primeira Responsabilidade

A primeira responsabilidade do pipeline será organizar todas as evidências recebidas.

Nenhuma interpretação será iniciada antes que todas as evidências estejam devidamente catalogadas.

Esse princípio garante:

- previsibilidade;
- auditabilidade;
- rastreabilidade;
- repetibilidade.

---

# Objetivo Final

Ao término do pipeline deverá existir exatamente um objeto:

```text
InterpreterResult
```

Todos os domínios da Plataforma DF Analysis IA consumirão exclusivamente esse contrato.

Nenhum domínio poderá consumir diretamente respostas de IA, OCR, XML Parser ou PDF Parser.

Essa regra reduz acoplamento e permite substituir mecanismos internos sem impactar os demais módulos da plataforma.

---

# Etapa 1 — Evidence Bundle

## Objetivo

Agrupar todas as evidências pertencentes a uma única comunicação.

O pipeline nunca trabalhará diretamente sobre arquivos isolados.

Todos os documentos serão encapsulados em um único objeto denominado:

```text
EvidenceBundle
```

Esse objeto representa o conjunto completo de evidências de um processo.

---

## Estrutura Conceitual

```text
EvidenceBundle

├── InboxMessage
├── InboxAttachment[]
├── Metadata
├── ParsedDocuments[]
├── Warnings[]
└── ProcessingHistory[]
```

---

## Responsabilidades

O EvidenceBundle deverá:

- preservar a comunicação original;
- preservar todos os anexos;
- registrar hashes;
- registrar metadados;
- registrar resultados intermediários;
- registrar advertências;
- registrar erros não fatais.

---

## Regra Fundamental

Nenhuma evidência original poderá ser modificada.

O pipeline trabalhará sempre sobre cópias lógicas das informações extraídas.

As evidências representam fatos.

Jamais poderão ser sobrescritas.

---

# Etapa 2 — Document Identification

## Objetivo

Identificar tecnicamente cada documento recebido.

Antes de interpretar o conteúdo é necessário conhecer o tipo documental.

Exemplos:

- E-mail
- PDF textual
- PDF digitalizado
- XML
- Excel
- CSV
- ZIP
- Imagem
- Documento desconhecido

---

## Estratégias

A identificação poderá utilizar:

- extensão;
- MIME Type;
- assinatura binária;
- estrutura interna;
- metadados;
- heurísticas.

---

## Resultado Esperado

Cada documento receberá uma classificação técnica.

Exemplo:

```text
Documento

↓

XML NFS-e
```

ou

```text
Documento

↓

PDF Digitalizado
```

Essa classificação definirá quais parsers serão utilizados nas próximas etapas.

---

# Etapa 3 — Deterministic Parsing

## Objetivo

Extrair informações estruturadas sem utilizar Inteligência Artificial.

Sempre que existir um parser confiável, ele deverá ser priorizado.

---

## XML

Pode extrair:

- Prestador
- Tomador
- CNPJ
- Valor
- Número da NFS-e
- Código de Verificação
- Competência
- ISS
- Descrição

---

## Excel

Pode extrair:

- Médicos
- Produção
- Valores
- Procedimentos
- Competência
- Totais

---

## PDF Textual

Pode extrair:

- Texto
- Tabelas
- Datas
- Valores
- Cabeçalhos

---

## PDF Digitalizado

Fluxo:

```text
PDF

↓

OCR

↓

Texto

↓

Parser
```

---

## E-mail

Pode extrair:

- remetente;
- destinatário;
- assunto;
- corpo;
- data;
- Message-ID;
- anexos.

---

# Regra de Ouro

Sempre utilizar parsing determinístico antes de IA.

A IA somente deverá ser utilizada quando o parser não conseguir responder adequadamente.

---

# Etapa 4 — Normalization

## Objetivo

Transformar diferentes representações para um formato único utilizado pelo domínio.

---

## Exemplos

CNPJ:

```text
61.590.410/0012-87

↓

61590410001287
```

Datas:

```text
13/07/2026

↓

2026-07-13
```

Competência:

```text
Junho/2026

↓

2026-06-01
```

Valores:

```text
R$ 12.350,90

↓

Decimal("12350.90")
```

---

## Outras normalizações

- remoção de espaços excedentes;
- deduplicação de médicos;
- padronização de nomenclaturas;
- padronização de hospitais;
- padronização de estabelecimentos;
- padronização de empresas.

---

## Resultado

Ao final desta etapa todas as informações deverão possuir representação única.

Isso simplifica significativamente as validações do domínio nas próximas fases do pipeline.

---

# Etapa 5 — Consolidation

## Objetivo

Consolidar todas as informações extraídas das diferentes evidências em uma única representação de negócio.

Esta etapa elimina redundâncias e organiza os dados provenientes de múltiplas fontes.

---

## Exemplo

Email

↓

Empresa = PRIME HEALTH

↓

Prazo = 13/07/2026

---

Excel

↓

Competência = Junho/2026

↓

Valor = R$ 124.580,22

---

XML

↓

Tomador

↓

Prestador

↓

Descrição

---

Resultado Consolidado

Empresa

Instituição

Estabelecimento

Competência

Valor

Descrição

Prazo

---

## Divergências

Quando existirem informações conflitantes, o pipeline deverá:

- preservar todas as versões;
- registrar a origem de cada informação;
- atribuir nível de confiança;
- encaminhar para validação.

Nenhuma informação deverá ser descartada automaticamente.

---

# Etapa 6 — Operational Classification

## Objetivo

Identificar qual processo operacional está sendo iniciado.

Exemplos:

- faturamento hospitalar;
- repasse médico;
- recebimento;
- cadastro;
- contrato;
- comercial;
- credenciamento.

---

## Estratégias

A classificação poderá utilizar:

- remetente;
- domínio do e-mail;
- assunto;
- conteúdo;
- anexos;
- empresas identificadas;
- estabelecimentos;
- regras determinísticas;
- Inteligência Artificial.

---

## Ordem de Prioridade

1. Regras determinísticas

2. Histórico conhecido

3. IA

4. Revisão humana

---

## Resultado

O pipeline produzirá um tipo operacional.

Exemplo:

```text
TipoOperationalCase

↓

FATURAMENTO_HOSPITALAR
```

---

# Etapa 7 — AI Enrichment

## Objetivo

Utilizar Inteligência Artificial para enriquecer informações que não puderam ser determinadas de forma totalmente confiável.

A IA poderá:

- sugerir empresa;
- sugerir estabelecimento;
- sugerir competência;
- sugerir descrição;
- interpretar contexto;
- identificar prioridade;
- detectar inconsistências;
- produzir observações.

---

## A IA não deverá

- emitir NFS-e;

- autorizar pagamentos;

- calcular repasses;

- sobrescrever evidências;

- alterar documentos originais;

- substituir regras de domínio.

---

## Confiança

Toda resposta produzida pela IA deverá possuir um indicador de confiança.

Exemplo

```text
Empresa

PRIME HEALTH

Confiança

0.97
```

---

# Etapa 8 — Business Validation

## Objetivo

Validar o resultado consolidado utilizando exclusivamente regras de negócio.

---

## Exemplos

Empresa cadastrada?

Competência válida?

Hospital conhecido?

Contrato ativo?

CNPJ consistente?

Valor permitido?

Duplicidade?

---

## Resultado

A validação poderá:

- aprovar;

- aprovar com ressalvas;

- solicitar revisão;

- rejeitar;

- registrar inconsistências.

---

## Princípio

A validação pertence ao domínio.

Nunca pertence à IA.

---

# Etapa 9 — InterpreterResult

## Objetivo

Produzir um único contrato estruturado para todos os domínios da plataforma.

O pipeline poderá utilizar diversos mecanismos internos.

Entretanto, sua saída será sempre um único objeto.

```text
InterpreterResult

├── BusinessExtraction

└── OperationalAnalysis
```

---

## BusinessExtraction

Representa os fatos extraídos da comunicação.

Exemplos:

- empresa;
- instituição;
- estabelecimento;
- competência;
- valor;
- descrição;
- médicos;
- documentos identificados.

---

## OperationalAnalysis

Representa a interpretação operacional produzida pelo pipeline.

Exemplos:

- necessita faturamento;
- necessita emissão de NFS-e;
- necessita envio;
- necessita recebimento;
- necessita repasse;
- prioridade;
- confiança;
- observações.

---

## Regra

Os domínios especializados nunca deverão consumir diretamente:

- GPT;
- Claude;
- Gemini;
- OCR;
- XML Parser;
- PDF Parser;
- Excel Parser.

Todos consumirão exclusivamente o contrato:

```text
InterpreterResult
```

---

# Etapa 10 — Persistência

O resultado validado deverá gerar uma:

```text
CommunicationInterpretation
```

A interpretação deverá registrar:

- mensagem de origem;
- engine utilizada;
- versão;
- método;
- confiança;
- sequência;
- data da interpretação;
- resultado estruturado.

Múltiplas interpretações poderão existir para a mesma comunicação.

---

# Etapa 11 — Encaminhamento Operacional

Após a validação, o domínio Operações decidirá o próximo passo.

Exemplos:

- abrir OperationalCase;
- solicitar revisão humana;
- aguardar complementação;
- descartar comunicação;
- encaminhar para outro domínio.

---

# Tratamento de Erros

O pipeline deverá distinguir claramente:

## Erros Técnicos

Exemplos:

- arquivo corrompido;
- OCR indisponível;
- timeout;
- parser inexistente.

---

## Divergências

Exemplos:

- CNPJ conflitante;
- competência divergente;
- valor incompatível.

---

## Informações Ausentes

Exemplos:

- empresa não identificada;
- competência ausente;
- estabelecimento não identificado.

---

## Baixa Confiança

Quando a confiança estiver abaixo do limite definido pela plataforma, o resultado deverá seguir para revisão humana.

---

# Auditoria

Cada etapa deverá registrar:

- horário de início;
- horário de término;
- duração;
- mecanismo utilizado;
- versão;
- entrada;
- saída;
- erros;
- advertências;
- correlation ID.

---

# Segurança

O pipeline deverá respeitar:

- LGPD;
- criptografia;
- rastreabilidade;
- mascaramento de dados sensíveis;
- controle de acesso;
- retenção de documentos;
- descarte seguro.

---

# Visão Geral Consolidada

```text
InboxMessage

↓

EvidenceBundle

↓

Document Identification

↓

Deterministic Parsing

↓

Normalization

↓

Consolidation

↓

Operational Classification

↓

AI Enrichment

↓

Business Validation

↓

InterpreterResult

↓

CommunicationInterpretation

↓

OperationalCase
```

---

# Princípio Fundamental

Sempre utilizar o mecanismo mais simples, previsível, auditável e determinístico capaz de resolver o problema.

A Inteligência Artificial deverá ser utilizada apenas quando agregar valor à interpretação.

Ela complementa o domínio.

Ela nunca substitui o domínio.