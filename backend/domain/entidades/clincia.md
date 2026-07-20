# Clínica

## Objetivo

Representa uma clínica que contrata serviços médicos ou atua como tomadora de serviços prestados por Empresas Médicas.

## Especialização

Herda os atributos da entidade Organização.

## Responsabilidades

- Contratar serviços médicos.
- Receber documentos fiscais.
- Disponibilizar informações para faturamento.
- Efetuar pagamentos aos prestadores.

## Relacionamentos

Uma Clínica pode:

- contratar diversas Empresas Médicas;
- receber diversas NFS-e;
- participar de processos administrativos;
- encaminhar solicitações de emissão.

## Papéis

Pode assumir os papéis de:

- Tomador
- Solicitante

## Regras de Negócio

- Deve possuir CNPJ válido.
- Pode possuir regras próprias de faturamento.
- Pode operar em um ou mais municípios.

## Observações

Embora possua características semelhantes às de um Hospital, a Clínica representa uma entidade distinta do domínio e pode possuir processos operacionais específicos.