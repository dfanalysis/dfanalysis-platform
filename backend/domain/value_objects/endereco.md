# Endereço

## Objetivo

Representa um endereço físico utilizado pelas entidades do domínio.

## Estrutura

Pode conter:

* logradouro;
* número;
* complemento;
* bairro;
* município;
* UF;
* CEP;
* país.

## Regras de Negócio

* Deve possuir município.
* Deve possuir UF.
* Deve possuir CEP quando aplicável.
* Deve ser imutável.

## Uso no Domínio

Pode compor:

* Empresa Médica;
* Hospital;
* Clínica;
* Cooperativa;
* Pessoa;
* Paciente.

## Observações

O Endereço é um Value Object composto por diversos atributos inseparáveis.
