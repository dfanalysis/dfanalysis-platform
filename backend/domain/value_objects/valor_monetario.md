# Valor Monetário

## Objetivo

Representa uma quantia financeira associada a uma moeda.

O Valor Monetário deve encapsular regras de precisão, arredondamento, comparação e cálculo financeiro.

## Estrutura

Um Valor Monetário possui:

* quantia;
* moeda.

Exemplo:

```text
R$ 202.699,00
```

Representação conceitual:

```text
quantia: 202699.00
moeda: BRL
```

## Regras de Negócio

* Deve utilizar tipo decimal de precisão fixa.
* Não deve utilizar ponto flutuante binário.
* Deve possuir moeda definida.
* Deve respeitar a quantidade de casas decimais da moeda.
* Dois valores são iguais quando possuem a mesma quantia e a mesma moeda.
* Operações entre moedas diferentes não devem ser permitidas sem conversão explícita.
* O Value Object deve ser imutável.

## Comportamentos Esperados

O Value Object deve ser capaz de:

* somar valores da mesma moeda;
* subtrair valores da mesma moeda;
* multiplicar por quantidade ou percentual;
* comparar valores;
* verificar se é positivo, negativo ou zero;
* aplicar arredondamento;
* retornar valor formatado;
* retornar representação normalizada.

## Uso no Domínio

O Valor Monetário pode representar:

* valor do serviço;
* base de cálculo;
* ISS;
* retenções;
* valor líquido;
* desconto;
* dedução;
* taxa administrativa;
* valor de repasse;
* valor de cobrança;
* valor pago.

## Arredondamento

O arredondamento deve ser explícito e seguir a regra definida para o contexto fiscal ou financeiro.

A plataforma não deve depender implicitamente do comportamento padrão da linguagem de programação.

## Observações

Sempre que possível, cálculos fiscais devem preservar maior precisão internamente e aplicar arredondamento apenas no ponto definido pela regra de negócio.

O valor monetário não deve carregar significado fiscal específico. Conceitos como imposto, desconto ou retenção devem ser representados pelo contexto em que o valor é utilizado.
