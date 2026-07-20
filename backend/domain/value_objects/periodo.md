# Período

## Objetivo

Representa um intervalo de tempo delimitado por uma data inicial e uma data final.

O Período é utilizado para representar a duração ou abrangência temporal de uma operação, produção, consulta ou documento.

## Estrutura

Um Período possui:

* data inicial;
* data final.

Exemplo:

```text
01/05/2026 a 31/05/2026
```

## Regras de Negócio

* A data inicial é obrigatória.
* A data final é obrigatória.
* A data final não pode ser anterior à data inicial.
* O período pode compreender um ou mais dias.
* O período pode atravessar meses ou anos.
* Dois períodos são iguais quando possuem a mesma data inicial e a mesma data final.
* O Value Object deve ser imutável.

## Comportamentos Esperados

O Value Object deve ser capaz de:

* validar a ordem das datas;
* calcular a duração;
* verificar se contém determinada data;
* verificar sobreposição com outro período;
* verificar se está contido em outro período;
* identificar interseção;
* retornar representação textual.

## Uso no Domínio

O Período pode representar:

* intervalo de prestação dos serviços;
* período de produção médica;
* intervalo de consulta de NFS-e;
* vigência de contrato;
* vigência de vínculo;
* período de apuração;
* janela de processamento;
* intervalo de relatório.

## Relação com Competência

Competência e Período não são sinônimos.

Uma Competência representa uma referência mensal.

Um Período representa um intervalo exato entre duas datas.

Exemplo:

```text
Competência: 2026-05
Período: 16/04/2026 a 15/05/2026
```

## Observações

A plataforma não deve presumir que todo Período corresponde ao primeiro e ao último dia de uma Competência.
