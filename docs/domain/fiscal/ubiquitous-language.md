# Linguagem Ubíqua — Domínio Fiscal

## Objetivo

Este documento define o vocabulário oficial do domínio fiscal da Plataforma DF Analysis IA.

Os termos registrados aqui deverão ser utilizados de forma consistente em:

- código-fonte;
- banco de dados;
- APIs;
- documentação;
- workflows;
- logs;
- integrações;
- testes;
- comunicação funcional e técnica.

## Princípios do domínio

1. O domínio fiscal é independente de fornecedor.
2. ISSNet, padrão nacional e demais provedores são integrações externas.
3. Os formatos XML e SOAP não determinam o modelo interno da plataforma.
4. Documentos fiscais devem possuir rastreabilidade completa.
5. Operações externas devem ser idempotentes.
6. Dados fiscais não devem ser alterados sem histórico e auditoria.
7. Empresa, prestador e tomador são conceitos distintos.
8. A NFS-e emitida deve ser separada da solicitação que originou sua emissão.

## Termos fundamentais

### Empresa

Organização cadastrada na Plataforma DF Analysis IA.

Uma empresa pode atuar como prestadora, tomadora ou intermediária de serviços, conforme o contexto da operação fiscal.

### Prestador

Pessoa jurídica ou pessoa física responsável pela prestação do serviço e pela emissão da NFS-e.

O prestador está vinculado a uma empresa cadastrada na plataforma.

### Tomador

Pessoa física ou jurídica que contrata ou recebe o serviço prestado.

### Intermediário

Pessoa física ou jurídica que participa da intermediação da prestação do serviço, quando aplicável.

### Serviço

Atividade executada pelo prestador em favor do tomador.

O serviço possui descrição, classificação fiscal, local de prestação, valor e regras tributárias.

### Competência

Data ou período em que ocorreu o fato gerador da prestação do serviço.

A competência não deve ser confundida com a data de emissão da NFS-e.

### Documento Provisório

Documento interno ou fiscal utilizado como origem da solicitação de emissão de uma NFS-e.

Pode ser representado externamente como RPS, DPS ou outro documento equivalente, conforme o provedor fiscal.

### RPS

Recibo Provisório de Serviços utilizado em integrações compatíveis com o padrão ABRASF 2.04 ou implementações municipais equivalentes.

### DPS

Declaração de Prestação de Serviços utilizada no padrão nacional da NFS-e e em integrações que adotem esse conceito.

### NFS-e

Nota Fiscal de Serviços Eletrônica gerada e autorizada pelo sistema fiscal competente.

A NFS-e possui existência digital e representa o resultado de uma operação fiscal concluída com sucesso.

### Série

Identificador associado à numeração de RPS, DPS ou documento equivalente.

### Número do Documento

Número sequencial que identifica um documento provisório dentro de sua série e contexto fiscal.

### Lote Fiscal

Agrupamento de documentos provisórios enviados conjuntamente para processamento por um provedor fiscal.

### Protocolo

Identificador fornecido pelo provedor fiscal após o recebimento de uma solicitação ou lote.

### Provedor Fiscal

Sistema externo responsável pelo processamento de documentos fiscais.

Exemplos:

- ISSNet;
- Ambiente Nacional da NFS-e;
- WebISS;
- GINFES;
- sistemas municipais próprios.

### Ambiente Fiscal

Ambiente externo no qual uma operação fiscal é executada.

Valores conceituais:

- homologação;
- produção.

### Solicitação de Emissão

Registro interno que representa o pedido para gerar uma NFS-e.

A solicitação existe antes do envio ao provedor fiscal e possui ciclo de vida próprio.

### Emissão

Processo de validação, preparação, transmissão e processamento de uma solicitação de NFS-e.

### Autorização

Resultado positivo do processamento fiscal, no qual o provedor gera uma NFS-e válida.

### Rejeição

Resultado negativo do processamento fiscal causado por erro estrutural, cadastral, tributário ou de negócio.

### Cancelamento

Evento fiscal que invalida uma NFS-e anteriormente autorizada, conforme regras do município ou provedor.

### Substituição

Operação que gera uma nova NFS-e em substituição a outra anteriormente emitida, preservando o vínculo entre ambas.

### Evento Fiscal

Ocorrência registrada após ou durante o ciclo de vida de um documento fiscal.

Exemplos:

- autorização;
- rejeição;
- cancelamento;
- substituição;
- consulta;
- contingência.

### Situação Fiscal

Estado atual de uma solicitação, documento provisório, lote ou NFS-e.

A situação fiscal deve ser representada por valores controlados e não por texto livre.

### Tributação

Conjunto de regras que determina a incidência, exigibilidade, retenção, base de cálculo, alíquota e valores dos tributos.

### ISSQN

Imposto Sobre Serviços de Qualquer Natureza incidente sobre determinadas prestações de serviços.

### Retenção

Valor tributário descontado ou recolhido pelo tomador, intermediário ou responsável tributário.

### Base de Cálculo

Valor utilizado como referência para cálculo de um tributo.

### Alíquota

Percentual aplicado sobre a base de cálculo para determinação do valor de um tributo.

### Valor Bruto

Valor integral do serviço antes de descontos, deduções e retenções.

### Valor Líquido

Valor resultante após descontos, deduções e retenções aplicáveis.

### Código de Tributação

Código utilizado para classificar fiscalmente o serviço conforme padrão nacional, municipal ou do provedor.

### Município de Incidência

Município ao qual o ISSQN é devido conforme a natureza e o local da prestação.

### Local da Prestação

Local em que o serviço foi efetivamente executado ou considerado prestado para fins fiscais.

### XML de Envio

Representação externa dos dados transmitidos ao provedor fiscal.

Não constitui o modelo interno do domínio.

### XML de Retorno

Representação externa da resposta recebida do provedor fiscal.

Deve ser preservado para rastreabilidade e auditoria.

### Payload Normalizado

Representação interna padronizada dos dados fiscais, independente do formato utilizado pelo provedor externo.

### Idempotência

Garantia de que a repetição controlada de uma mesma solicitação não produzirá documentos fiscais duplicados.

### Auditoria Fiscal

Registro cronológico e imutável das ações, alterações, transmissões e respostas relacionadas ao processo fiscal.

### Correlação

Identificador interno utilizado para relacionar solicitação, documento provisório, transmissão, protocolo, resposta e NFS-e.

## Termos que não devem ser tratados como sinônimos

- Empresa não é necessariamente Prestador.
- Competência não é Data de Emissão.
- Solicitação de Emissão não é NFS-e.
- Documento Provisório não é NFS-e.
- Rejeição não é Erro Interno.
- Cancelamento não é Exclusão.
- Provedor Fiscal não é Município.
- XML não é Entidade de Domínio.
- RPS e DPS não são necessariamente o mesmo formato externo.

## Evolução do documento

Novos termos deverão ser incluídos antes ou durante a implementação de funcionalidades que introduzam novos conceitos de negócio.

Alterações relevantes nesta linguagem deverão ser avaliadas quanto ao impacto em:

- models;
- schemas;
- migrations;
- endpoints;
- integrações;
- logs;
- testes;
- documentação.
