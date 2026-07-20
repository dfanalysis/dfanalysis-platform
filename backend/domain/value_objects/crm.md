# CRM

## Objetivo

Representa o registro profissional de um médico perante o Conselho Regional de Medicina.

## Estrutura

É composto por:

* número do registro;
* UF do conselho.

Exemplo:

```text
CRM-DF 12345
```

Representação conceitual:

```text
numero: 12345
uf: DF
```

## Regras de Negócio

* Deve possuir número válido.
* Deve possuir UF válida.
* Deve ser imutável.
* Dois CRMs são iguais quando possuem o mesmo número e UF.

## Uso no Domínio

Identifica o Médico.

## Observações

O mesmo número pode existir em estados diferentes.

Por isso, número e UF formam conjuntamente a identidade do registro.
