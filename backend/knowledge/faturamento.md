# Macroprocesso: Faturamento

## Objetivo

O macroprocesso de Faturamento compreende todas as atividades relacionadas à emissão de documentos fiscais destinados ao recebimento dos serviços prestados pelas empresas médicas administradas pela DF Analysis.

Este macroprocesso representa uma das principais fontes de entrada de receitas das empresas médicas e constitui o ponto de partida para diversos processos subsequentes, como financeiro, conciliação bancária, cobrança, repasse médico, contabilidade e obrigações fiscais.

---

# Escopo

O macroprocesso de Faturamento contempla:

- Recebimento de solicitações de emissão;
- Identificação da empresa emissora;
- Identificação do tomador do serviço;
- Validação dos documentos recebidos;
- Identificação da modalidade de faturamento;
- Definição da competência;
- Geração da descrição dos serviços;
- Emissão da Nota Fiscal de Serviços Eletrônica (NFS-e);
- Envio da NFS-e ao solicitante;
- Registro para processos financeiros e contábeis.

---

# Modalidades

Atualmente o macroprocesso de Faturamento contempla as seguintes modalidades:

## Produção Hospitalar

Corresponde às situações em que hospitais, clínicas ou instituições de saúde realizam a apuração da produção médica e posteriormente solicitam a emissão de Nota Fiscal pela empresa médica referente aos honorários devidos ao profissional.

Fluxo simplificado:

Hospital / Clínica

↓

Apuração da Produção Médica

↓

Solicitação de Emissão de NFS-e

↓

Empresa Médica

↓

Emissão da NFS-e

↓

Recebimento Financeiro

---

## Atendimento Particular

Corresponde aos atendimentos particulares realizados diretamente ao paciente.

Neste cenário a Nota Fiscal é emitida diretamente para o CPF do paciente.

Fluxo simplificado:

Paciente

↓

Prestação do Serviço

↓

Emissão da NFS-e

↓

Recebimento Financeiro

---

## Outras modalidades

O macroprocesso foi concebido para suportar futuramente outras modalidades, tais como:

- Plantões;
- Cooperativas;
- Convênios Diretos;
- Empresas Privadas;
- Outros modelos de prestação de serviços.

---

# Fora do Escopo

Este macroprocesso NÃO contempla o faturamento assistencial realizado por clínicas e hospitais perante operadoras de planos de saúde.

Esse processo envolve atividades como:

- faturamento TISS;
- processamento de guias;
- geração de XML TISS;
- auditoria médica;
- glosas;
- reapresentações;
- protocolos junto às operadoras.

Embora a DF Analysis também atue nesse segmento, trata-se de um módulo independente da Plataforma DF Analysis IA, denominado provisoriamente como "Faturamento Assistencial".

---

# Sistemas envolvidos

Dependendo da modalidade poderão ser utilizados:

- ISSNET;
- Sistema Nacional NFS-e;
- ERP da empresa médica;
- Sistemas Hospitalares;
- Planilhas;
- Correio eletrônico;
- WhatsApp;
- APIs.

---

# Entradas

As solicitações podem ser recebidas através de:

- E-mail;
- WhatsApp;
- ERP;
- API;
- Portal do Hospital;
- Portal da Clínica.

---

# Saídas

O macroprocesso gera como principais saídas:

- NFS-e emitida;
- XML da NFS-e;
- PDF da NFS-e;
- Protocolo de emissão;
- Registro para o módulo financeiro;
- Registro para o módulo contábil;
- Registro para auditoria.

---

# Objetivo da IA

A Inteligência Artificial deverá ser capaz de:

- identificar automaticamente a modalidade de faturamento;
- interpretar documentos recebidos;
- identificar dados obrigatórios;
- detectar inconsistências;
- sugerir descrições fiscais;
- identificar competência;
- validar tomador;
- auxiliar na emissão automática da NFS-e.

---

# Observações

Este documento representa a definição oficial do macroprocesso de Faturamento da Plataforma DF Analysis IA.

Todas as regras específicas deverão ser documentadas em arquivos próprios dentro da Base de Conhecimento.