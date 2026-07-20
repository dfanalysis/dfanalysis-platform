# Empresa Médica

## Objetivo

Representa a pessoa jurídica do responsável pela prestação de serviços médicos.

É a principal entidade de negócio da Plataforma DF Analysis IA, pois concentra os processos administrativos, fiscais, financeiros e comerciais relacionados aos médicos clientes.

## Especialização

Herda os atributos da entidade Organização.

## Responsabilidades

- Emitir NFS-e.
- Receber solicitações de emissão.
- Manter cadastro fiscal.
- Relacionar-se com hospitais, clínicas e pacientes.
- Centralizar os processos administrativos da empresa.

## Relacionamentos

Uma Empresa Médica pode:

- possuir um ou mais médicos vinculados;
- possuir usuários da plataforma;
- possuir diversas Solicitações de Emissão;
- emitir diversas NFS-e;
- atender diversos tomadores;
- participar de diversos processos administrativos.

## Papéis

Pode assumir os papéis de:

- Prestador
- Solicitante

## Regras de Negócio

- Deve possuir CNPJ válido.
- Deve estar ativa para emissão de NFS-e.
- Deve possuir configuração fiscal válida.
- Pode possuir mais de um certificado digital.
- Pode emitir notas para diversos municípios (futuramente).

## Observações

A Empresa Médica é uma entidade central do domínio e funciona como Aggregate Root para diversos processos administrativos da plataforma.