# ADR-007 — Solicitação de Emissão como Aggregate Root

## Status

Aceito

## Contexto

O processo fiscal da Plataforma DF Analysis IA não começa pela NFS-e emitida.

A NFS-e é o resultado de um fluxo que pode envolver:

- recebimento da solicitação;
- validação cadastral;
- validação fiscal;
- preparação dos dados;
- geração de RPS ou DPS;
- transmissão ao provedor fiscal;
- processamento;
- autorização ou rejeição;
- armazenamento dos retornos;
- auditoria;
- eventual reprocessamento.

As solicitações poderão ter diferentes origens, como:

- API;
- portal;
- e-mail;
- WhatsApp;
- ERP;
- workflow do n8n;
- agente de IA;
- importação de arquivos.

Modelar a NFS-e como entidade central faria o domínio depender excessivamente do resultado final e dificultaria o tratamento de solicitações ainda não emitidas, rejeitadas, reprocessadas ou canceladas.

## Decisão

A entidade `SolicitacaoEmissao` será o Aggregate Root do processo de emissão fiscal.

Ela será responsável por controlar o ciclo de vida da emissão, incluindo:

- empresa responsável;
- prestador;
- tomador;
- serviço;
- competência;
- valores;
- tributação;
- origem da solicitação;
- situação do processamento;
- correlação;
- idempotência;
- documento provisório;
- protocolo;
- eventos fiscais;
- retorno do provedor;
- vínculo com a NFS-e emitida.

A NFS-e será tratada como resultado fiscal da solicitação, e não como ponto de entrada do processo.

## Consequências positivas

- independência em relação ao ISSNet;
- suporte a múltiplos provedores fiscais;
- suporte a múltiplos canais de entrada;
- rastreabilidade completa;
- reprocessamento controlado;
- prevenção de emissão duplicada;
- auditoria do ciclo de vida;
- separação entre solicitação e documento autorizado;
- expansão futura para DPS e padrão nacional.

## Consequências negativas

- maior quantidade de estados internos;
- necessidade de controlar transições de situação;
- maior complexidade inicial do modelo;
- necessidade de eventos e histórico de processamento;
- necessidade de políticas claras de idempotência.

## Regras arquiteturais

1. A NFS-e não poderá existir no domínio sem vínculo com uma solicitação de emissão, salvo processos futuros de importação ou sincronização externa.
2. O domínio não dependerá diretamente de XML, SOAP ou estruturas específicas do ISSNet.
3. Toda integração externa deverá ocorrer por adaptadores.
4. Cada solicitação deverá possuir um identificador de correlação.
5. Cada solicitação deverá possuir uma chave de idempotência quando aplicável.
6. Mudanças de situação deverão ser controladas pelo domínio.
7. Retornos externos deverão ser armazenados para auditoria.
8. Exclusões físicas de registros fiscais não serão permitidas no fluxo operacional normal.

## Fluxo conceitual

```text
Origem da solicitação
        ↓
Solicitação de Emissão
        ↓
Validação
        ↓
Documento Provisório
        ↓
Transmissão
        ↓
Provedor Fiscal
        ↓
Autorização ou Rejeição
        ↓
NFS-e e Eventos Fiscais