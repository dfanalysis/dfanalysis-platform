# CPF

## Objetivo

Representa o número de inscrição de uma pessoa física no Cadastro de Pessoas Físicas.

O CPF é um Value Object porque é definido integralmente pelo seu valor e não possui identidade própria.

## Estrutura

O CPF deve possuir 11 dígitos numéricos.

Exemplo:

```text
047.867.609-35
```

Forma normalizada:

```text
04786760935
```

## Regras de Negócio

* Deve possuir exatamente 11 dígitos.
* Deve conter apenas caracteres numéricos após normalização.
* Deve possuir dígitos verificadores válidos.
* Não deve aceitar sequências repetitivas inválidas.
* Deve ser armazenado preferencialmente sem máscara.
* A máscara deve ser aplicada apenas na apresentação.
* Dois CPFs são iguais quando seus valores normalizados forem iguais.

## Comportamentos Esperados

O Value Object deve ser capaz de:

* normalizar o valor;
* validar o formato;
* validar os dígitos verificadores;
* retornar o valor sem máscara;
* retornar o valor formatado;
* comparar igualdade por valor.

## Uso no Domínio

O CPF pode identificar:

* Médico;
* Paciente;
* Solicitante pessoa física;
* Usuário;
* Tomador pessoa física;
* representante de uma Organização.

## Observações

O CPF deve ser representado como texto imutável.

Nunca deve ser convertido para número inteiro, pois pode possuir zeros à esquerda e não representa uma quantidade matemática.
