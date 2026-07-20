# Competência

## Objetivo

Representa o período de referência econômica, contábil, fiscal ou operacional ao qual uma prestação de serviços pertence.

A Competência não deve ser confundida com a data de emissão da NFS-e nem com a data de pagamento.

## Estrutura

A Competência normalmente é representada por:

* mês;
* ano.

Exemplo:

```text
Maio de 2026
```

Forma normalizada:

```text
2026-05
```

## Regras de Negócio

* Deve possuir mês válido entre 1 e 12.
* Deve possuir ano válido.
* Deve representar um período mensal único.
* Deve ser imutável.
* Duas competências são iguais quando possuem o mesmo mês e ano.
* Não deve depender da data de criação do registro.
* Pode ser anterior à data de emissão da NFS-e.
* Pode ser determinada a partir do período informado pelo Tomador ou da ocorrência do fato gerador.

## Comportamentos Esperados

O Value Object deve ser capaz de:

* validar mês e ano;
* retornar o primeiro dia da competência;
* retornar o último dia da competência;
* comparar competências;
* identificar competência anterior e posterior;
* converter para representação textual;
* converter para formato normalizado.

## Uso no Domínio

A Competência pode estar associada a:

* Solicitação de Emissão;
* produção médica;
* relatório de produção;
* NFS-e;
* repasse médico;
* cobrança;
* fechamento mensal;
* relatório financeiro.

## Exemplos

Uma prestação pode ocorrer em maio de 2026, enquanto:

* a solicitação é recebida em junho de 2026;
* a NFS-e é emitida em junho de 2026;
* o pagamento é realizado em julho de 2026.

Nesse caso, a competência permanece:

```text
2026-05
```

## Observações

A Competência deve ser tratada como conceito explícito do domínio para evitar inferências incorretas baseadas na data de emissão ou pagamento.
