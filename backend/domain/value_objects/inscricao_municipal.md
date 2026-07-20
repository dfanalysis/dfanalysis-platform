# Inscrição Municipal

## Objetivo

Representa a inscrição municipal de um contribuinte perante o município responsável pela tributação do ISS.

## Estrutura

É composta por uma sequência de caracteres definida pelo município.

Exemplos:

* 0766024100100
* 0757742800286

## Regras de Negócio

* Deve possuir valor válido para o município correspondente.
* Pode possuir zeros à esquerda.
* Deve ser armazenada exatamente como fornecida pelo município.
* Deve ser tratada como texto.
* Deve ser imutável.

## Uso no Domínio

Pode identificar:

* Prestador
* Tomador
* Organização
* Empresa Médica
* Hospital
* Clínica

## Observações

Cada município possui regras próprias de composição da Inscrição Municipal.

A plataforma não deve assumir tamanho ou formato fixo.
