# CNPJ

## Objetivo

Representa o número de inscrição de uma pessoa jurídica no Cadastro Nacional da Pessoa Jurídica.

O CNPJ é um Value Object porque sua validade e significado dependem exclusivamente do valor informado, sem possuir identidade própria.

## Estrutura

O CNPJ deve possuir 14 dígitos numéricos.

Exemplo:

```text
12.971.279/0001-30
```

Forma normalizada:

```text
12971279000130
```

## Regras de Negócio

* Deve possuir exatamente 14 dígitos.
* Deve conter apenas caracteres numéricos após normalização.
* Deve possuir dígitos verificadores válidos.
* Não deve aceitar sequências inválidas ou repetitivas.
* Deve ser armazenado preferencialmente sem máscara.
* A máscara deve ser aplicada apenas na apresentação.
* Dois CNPJs são iguais quando seus valores normalizados forem iguais.

## Comportamentos Esperados

O Value Object deve ser capaz de:

* normalizar o valor;
* validar o formato;
* validar os dígitos verificadores;
* retornar o valor sem máscara;
* retornar o valor formatado;
* comparar igualdade por valor.

## Uso no Domínio

O CNPJ pode identificar:

* Empresa Médica;
* Hospital;
* Clínica;
* Cooperativa;
* Tomador pessoa jurídica;
* Prestador;
* Organização;
* contribuinte cadastrado no município.

## Observações

O CNPJ não deve ser tratado como número inteiro, pois:

* pode possuir zeros à esquerda;
* não participa de operações matemáticas;
* possui regras próprias de formatação e validação.

Deve ser representado como texto imutável.
