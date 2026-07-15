# Event Storming — Plataforma DF Analysis IA

## Objetivo

Este documento registra os principais eventos de domínio identificados na operação da DF Analysis.

Os eventos representam fatos que ocorreram no negócio. Não representam telas, endpoints, tabelas ou ferramentas específicas.

---

# Fluxo operacional principal

## Evento 01 — EntradaRecebida

Uma nova entrada foi recebida pela plataforma.

Possíveis canais:

- e-mail;
- API;
- webhook;
- upload;
- WhatsApp;
- integração com ERP;
- lançamento manual.

Domínio responsável: Operações.

---

## Evento 02 — AnexosImportados

Os arquivos vinculados à entrada foram armazenados e associados à mensagem original.

Exemplos:

- PDF;
- Excel;
- XML;
- CSV;
- imagem;
- documento textual.

Domínio responsável: Operações.

---

## Evento 03 — DocumentosClassificados

Os documentos recebidos foram classificados conforme sua finalidade operacional.

Exemplos:

- demonstrativo financeiro;
- produção analítica;
- relação de pacientes;
- relação de consultas;
- relação de taxas;
- relatório de descontos;
- solicitação de faturamento;
- NFS-e;
- XML fiscal;
- comprovante bancário.

Domínio responsável: Operações.

---

## Evento 04 — EmpresaPrestadoraIdentificada

A empresa médica responsável pelo faturamento foi identificada.

A identificação poderá ocorrer por:

- CNPJ;
- razão social;
- nome de sócio ou médico de referência;
- histórico do remetente;
- contrato operacional;
- conteúdo dos anexos.

Domínio responsável: Cadastro e Operações.

---

## Evento 05 — InstituicaoIdentificada

A instituição contratante ou grupo hospitalar foi identificado.

Exemplos:

- Hospital Sírio-Libanês;
- Rede D'Or;
- Rede Ímpar;
- Hospital Santa Lúcia;
- Dasa.

Domínio responsável: Instituições.

---

## Evento 06 — EstabelecimentoIdentificado

O estabelecimento fiscal tomador foi identificado.

Um estabelecimento pode possuir:

- CNPJ próprio;
- inscrição municipal própria;
- endereço próprio;
- regras próprias de faturamento;
- canal próprio de envio de documentos.

Domínio responsável: Instituições.

---

## Evento 07 — ContratoOperacionalIdentificado

A relação operacional entre empresa prestadora, estabelecimento e tipo de serviço foi identificada.

O contrato operacional poderá determinar:

- tipo de produção;
- modelo de descrição fiscal;
- prazo;
- janela de emissão;
- documentos obrigatórios;
- canal de envio;
- regras tributárias;
- regras de repasse.

Domínio responsável: Instituições e Contratos Operacionais.

---

## Evento 08 — DemandaOperacionalCriada

A entrada recebida foi transformada em uma demanda operacional estruturada.

A demanda preserva:

- origem;
- mensagem original;
- anexos;
- empresa;
- instituição;
- estabelecimento;
- competência;
- prazo;
- processo hospitalar;
- situação da conferência.

Domínio responsável: Operações.

---

## Evento 09 — ProducaoMedicaInterpretada

Os itens de produção médica foram extraídos, classificados e relacionados.

Possíveis informações:

- médico executor;
- paciente;
- procedimento;
- código TUSS;
- data de execução;
- quantidade;
- valor;
- convênio;
- estabelecimento;
- competência.

Domínio responsável: Produção Médica.

---

## Evento 10 — FaturamentoAutorizado

A conferência operacional determinou que os valores e documentos estão aptos para faturamento.

Esse evento representa uma decisão de negócio anterior à emissão fiscal.

Domínio responsável: Operações e Produção Médica.

---

## Evento 11 — SolicitacaoEmissaoCriada

Uma solicitação interna de emissão fiscal foi criada.

Ela deverá conter somente as informações necessárias ao domínio Fiscal e referências aos agregados anteriores.

Domínio responsável: Fiscal.

---

## Evento 12 — SolicitacaoValidada

A solicitação passou pelas validações internas de empresa, competência, valor, descrição, status e idempotência.

Domínio responsável: Fiscal.

---

## Evento 13 — DocumentoProvisorioGerado

Um RPS ou DPS foi gerado para transmissão ao provedor municipal ou nacional.

Domínio responsável: Fiscal.

---

## Evento 14 — NFSeEmitida

A NFS-e foi autorizada pelo provedor fiscal.

Informações esperadas:

- número;
- código de verificação;
- protocolo;
- XML;
- PDF;
- data de emissão;
- valor;
- tomador;
- retenções.

Domínio responsável: Fiscal.

---

## Evento 15 — NFSeEnviadaAoTomador

A nota fiscal e os documentos exigidos foram encaminhados ao hospital, clínica ou instituição.

Domínio responsável: Operações e Fiscal.

---

## Evento 16 — ContaReceberCriada

A emissão da NFS-e originou um recebível financeiro.

Domínio responsável: Financeiro.

---

## Evento 17 — PagamentoIdentificado

Um crédito bancário possivelmente relacionado a uma ou mais NFS-e foi identificado.

Domínio responsável: Financeiro.

---

## Evento 18 — RecebimentoConciliado

O pagamento bancário foi vinculado ao recebível e às respectivas NFS-e.

Domínio responsável: Financeiro.

---

## Evento 19 — RecebivelBaixado

A conta a receber foi considerada liquidada.

Domínio responsável: Financeiro.

---

## Evento 20 — GrupoRepasseCriado

Foi criado um agrupamento para cálculo do valor devido ao médico.

O grupo poderá consolidar:

- produções;
- NFS-e;
- recebimentos;
- competências;
- tipos de serviço;
- taxas;
- descontos;
- acréscimos.

Domínio responsável: Repasse Médico.

---

## Evento 21 — RepasseCalculado

As regras de remuneração, taxas e descontos foram aplicadas.

Domínio responsável: Repasse Médico.

---

## Evento 22 — RepasseAprovado

O cálculo do repasse foi conferido e autorizado para pagamento.

Domínio responsável: Repasse Médico.

---

## Evento 23 — RepassePago

O pagamento ao médico foi realizado e seu comprovante foi armazenado.

Domínio responsável: Repasse Médico.

---

## Evento 24 — ProcessoEncerrado

O ciclo operacional foi concluído com rastreabilidade entre:

- entrada;
- produção;
- faturamento;
- NFS-e;
- recebimento;
- repasse;
- pagamento ao médico.

---

# Fluxo resumido

```text
EntradaRecebida
    ↓
AnexosImportados
    ↓
DocumentosClassificados
    ↓
EmpresaPrestadoraIdentificada
    ↓
EstabelecimentoIdentificado
    ↓
ContratoOperacionalIdentificado
    ↓
DemandaOperacionalCriada
    ↓
ProducaoMedicaInterpretada
    ↓
FaturamentoAutorizado
    ↓
SolicitacaoEmissaoCriada
    ↓
NFSeEmitida
    ↓
ContaReceberCriada
    ↓
PagamentoIdentificado
    ↓
RecebimentoConciliado
    ↓
GrupoRepasseCriado
    ↓
RepasseCalculado
    ↓
RepassePago
    ↓
ProcessoEncerrado
